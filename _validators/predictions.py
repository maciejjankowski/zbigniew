#!/usr/bin/env python3
"""
ZBIGNIEW Prediction Tracker

Tracks predictions, monitors deadlines, analyzes calibration.
Outputs reports for accuracy tracking and calibration analysis.
"""

import json
import sys
from datetime import datetime, date, timedelta
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from collections import defaultdict

# ANSI colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'


@dataclass
class Prediction:
    id: str
    text: str
    deadline: date
    confidence: int
    confidence_pct: int
    category: str
    vectors: list[str]
    falsification: str
    status: str
    created: Optional[date] = None
    resolution_date: Optional[date] = None
    resolution_notes: Optional[str] = None
    assessment_ref: Optional[str] = None

    @property
    def days_until_deadline(self) -> int:
        return (self.deadline - date.today()).days

    @property
    def is_overdue(self) -> bool:
        return self.days_until_deadline < 0 and self.status == 'active'

    @property
    def is_due_soon(self) -> bool:
        return 0 <= self.days_until_deadline <= 30 and self.status == 'active'


@dataclass
class CalibrationBucket:
    """Tracks predictions in a probability range for calibration."""
    range_low: int
    range_high: int
    predictions: list[Prediction] = field(default_factory=list)

    @property
    def total(self) -> int:
        return len(self.predictions)

    @property
    def confirmed(self) -> int:
        return sum(1 for p in self.predictions if p.status == 'confirmed')

    @property
    def resolved(self) -> int:
        return sum(1 for p in self.predictions if p.status in ['confirmed', 'refuted'])

    @property
    def actual_rate(self) -> Optional[float]:
        if self.resolved == 0:
            return None
        return self.confirmed / self.resolved

    @property
    def expected_rate(self) -> float:
        return (self.range_low + self.range_high) / 200  # Midpoint as decimal

    @property
    def calibration_error(self) -> Optional[float]:
        if self.actual_rate is None:
            return None
        return self.actual_rate - self.expected_rate


class PredictionTracker:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.predictions: list[Prediction] = []
        self.load_predictions()

    def load_predictions(self):
        """Load predictions from active.jsonl."""
        pred_path = self.base_path / '_predictions' / 'active.jsonl'
        if not pred_path.exists():
            print(f"{RED}Error: {pred_path} not found{RESET}")
            return

        with open(pred_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    if obj.get('_schema'):
                        continue

                    pred = Prediction(
                        id=obj['id'],
                        text=obj['prediction'],
                        deadline=datetime.strptime(obj['deadline'], '%Y-%m-%d').date(),
                        confidence=obj['confidence'],
                        confidence_pct=obj['confidence_pct'],
                        category=obj['category'],
                        vectors=obj['vectors'],
                        falsification=obj['falsification'],
                        status=obj['status'],
                        created=datetime.fromisoformat(obj['created']).date() if 'created' in obj else None,
                        resolution_date=datetime.strptime(obj['resolution_date'], '%Y-%m-%d').date() if obj.get('resolution_date') else None,
                        resolution_notes=obj.get('resolution_notes'),
                        assessment_ref=obj.get('assessment_ref'),
                    )
                    self.predictions.append(pred)
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"{YELLOW}Warning: Could not parse prediction: {e}{RESET}")

    def get_active(self) -> list[Prediction]:
        return [p for p in self.predictions if p.status == 'active']

    def get_overdue(self) -> list[Prediction]:
        return [p for p in self.predictions if p.is_overdue]

    def get_due_soon(self, days: int = 30) -> list[Prediction]:
        return [p for p in self.predictions
                if p.status == 'active' and 0 <= p.days_until_deadline <= days]

    def get_resolved(self) -> list[Prediction]:
        return [p for p in self.predictions if p.status in ['confirmed', 'refuted']]

    def get_by_category(self) -> dict[str, list[Prediction]]:
        by_cat = defaultdict(list)
        for p in self.predictions:
            by_cat[p.category].append(p)
        return dict(by_cat)

    def get_by_vector(self) -> dict[str, list[Prediction]]:
        by_vec = defaultdict(list)
        for p in self.predictions:
            for v in p.vectors:
                by_vec[v].append(p)
        return dict(by_vec)

    def get_calibration_buckets(self) -> list[CalibrationBucket]:
        """Group predictions into probability buckets for calibration analysis."""
        buckets = [
            CalibrationBucket(1, 25),
            CalibrationBucket(25, 50),
            CalibrationBucket(50, 75),
            CalibrationBucket(75, 90),
            CalibrationBucket(90, 99),
        ]

        for pred in self.predictions:
            pct = pred.confidence_pct
            for bucket in buckets:
                if bucket.range_low <= pct <= bucket.range_high:
                    bucket.predictions.append(pred)
                    break

        return buckets

    def print_status_report(self):
        """Print comprehensive status report."""
        print(f"\n{BOLD}{'=' * 60}{RESET}")
        print(f"{BOLD}ZBIGNIEW PREDICTION TRACKER{RESET}")
        print(f"{BOLD}{'=' * 60}{RESET}")
        print(f"Report date: {date.today()}")
        print(f"Total predictions: {len(self.predictions)}")
        print()

        # Summary stats
        active = len(self.get_active())
        confirmed = sum(1 for p in self.predictions if p.status == 'confirmed')
        refuted = sum(1 for p in self.predictions if p.status == 'refuted')
        expired = sum(1 for p in self.predictions if p.status == 'expired')

        print(f"{CYAN}STATUS SUMMARY{RESET}")
        print(f"  Active:    {active}")
        print(f"  Confirmed: {GREEN}{confirmed}{RESET}")
        print(f"  Refuted:   {RED}{refuted}{RESET}")
        print(f"  Expired:   {YELLOW}{expired}{RESET}")

        # Accuracy (if any resolved)
        resolved = confirmed + refuted
        if resolved > 0:
            accuracy = confirmed / resolved
            print(f"\n{CYAN}ACCURACY{RESET}")
            print(f"  Resolved: {resolved}")
            print(f"  Accuracy: {accuracy:.1%}")

        # Overdue predictions
        overdue = self.get_overdue()
        if overdue:
            print(f"\n{RED}{BOLD}OVERDUE PREDICTIONS (requires action){RESET}")
            for p in overdue:
                days = abs(p.days_until_deadline)
                print(f"  {RED}✗{RESET} [{p.id}] {days} days overdue")
                print(f"      {p.text[:60]}...")

        # Due soon
        due_soon = self.get_due_soon(30)
        if due_soon:
            print(f"\n{YELLOW}DEADLINES APPROACHING (next 30 days){RESET}")
            for p in sorted(due_soon, key=lambda x: x.deadline):
                print(f"  {YELLOW}⚠{RESET} [{p.id}] {p.days_until_deadline} days ({p.deadline})")
                print(f"      {p.text[:60]}...")
                print(f"      Confidence: {p.confidence_pct}%")

        # All active by deadline
        print(f"\n{CYAN}ALL ACTIVE PREDICTIONS{RESET}")
        for p in sorted(self.get_active(), key=lambda x: x.deadline):
            status_color = YELLOW if p.is_due_soon else BLUE
            print(f"  {status_color}●{RESET} [{p.id}] {p.deadline} ({p.days_until_deadline}d)")
            print(f"      {p.text[:70]}...")
            print(f"      Confidence: {p.confidence_pct}% | Category: {p.category}")

    def print_calibration_report(self):
        """Print calibration analysis."""
        print(f"\n{BOLD}{'=' * 60}{RESET}")
        print(f"{BOLD}CALIBRATION ANALYSIS{RESET}")
        print(f"{BOLD}{'=' * 60}{RESET}")
        print()
        print("Goal: Predictions at X% confidence should be correct X% of the time.")
        print()

        buckets = self.get_calibration_buckets()

        print(f"{'Range':<12} {'Total':<8} {'Resolved':<10} {'Confirmed':<10} {'Expected':<10} {'Actual':<10} {'Error':<10}")
        print("-" * 70)

        for bucket in buckets:
            range_str = f"{bucket.range_low}-{bucket.range_high}%"
            expected_str = f"{bucket.expected_rate:.0%}"

            if bucket.actual_rate is not None:
                actual_str = f"{bucket.actual_rate:.0%}"
                error = bucket.calibration_error
                if abs(error) <= 0.1:
                    error_color = GREEN
                elif abs(error) <= 0.2:
                    error_color = YELLOW
                else:
                    error_color = RED
                error_str = f"{error_color}{error:+.0%}{RESET}"
            else:
                actual_str = "-"
                error_str = "-"

            print(f"{range_str:<12} {bucket.total:<8} {bucket.resolved:<10} {bucket.confirmed:<10} {expected_str:<10} {actual_str:<10} {error_str}")

        resolved_total = sum(b.resolved for b in buckets)
        if resolved_total < 10:
            print(f"\n{YELLOW}Note: Need more resolved predictions for meaningful calibration analysis.{RESET}")
            print(f"Currently: {resolved_total} resolved. Recommend: 20+ per bucket.")

    def print_vector_report(self):
        """Print predictions grouped by vector."""
        print(f"\n{BOLD}PREDICTIONS BY VECTOR{RESET}")
        by_vector = self.get_by_vector()
        for vector, preds in sorted(by_vector.items()):
            active = sum(1 for p in preds if p.status == 'active')
            confirmed = sum(1 for p in preds if p.status == 'confirmed')
            print(f"  {vector}: {len(preds)} total ({active} active, {confirmed} confirmed)")

    def export_accuracy_update(self) -> str:
        """Generate markdown for accuracy.md update."""
        lines = [
            f"# PREDICTION ACCURACY TRACKER",
            f"",
            f"*Updated: {date.today()}*",
            f"",
            f"---",
            f"",
            f"## OVERALL STATISTICS",
            f"",
            f"| Metric | Count | Percentage |",
            f"|--------|-------|------------|",
        ]

        total = len(self.predictions)
        confirmed = sum(1 for p in self.predictions if p.status == 'confirmed')
        refuted = sum(1 for p in self.predictions if p.status == 'refuted')
        expired = sum(1 for p in self.predictions if p.status == 'expired')
        active = sum(1 for p in self.predictions if p.status == 'active')

        resolved = confirmed + refuted
        accuracy = f"{confirmed/resolved:.0%}" if resolved > 0 else "-"

        lines.append(f"| Total Predictions | {total} | - |")
        lines.append(f"| Confirmed | {confirmed} | {confirmed/total:.0%} |" if total > 0 else "| Confirmed | 0 | 0% |")
        lines.append(f"| Refuted | {refuted} | {refuted/total:.0%} |" if total > 0 else "| Refuted | 0 | 0% |")
        lines.append(f"| Expired | {expired} | {expired/total:.0%} |" if total > 0 else "| Expired | 0 | 0% |")
        lines.append(f"| Active | {active} | {active/total:.0%} |" if total > 0 else "| Active | 0 | 100% |")

        return "\n".join(lines)


def main():
    script_dir = Path(__file__).parent
    base_path = script_dir.parent

    tracker = PredictionTracker(base_path)

    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == 'calibration':
            tracker.print_calibration_report()
        elif cmd == 'vectors':
            tracker.print_vector_report()
        elif cmd == 'overdue':
            overdue = tracker.get_overdue()
            if overdue:
                for p in overdue:
                    print(f"{p.id}: {p.text}")
            else:
                print("No overdue predictions.")
        elif cmd == 'export':
            print(tracker.export_accuracy_update())
        else:
            print(f"Unknown command: {cmd}")
            print("Commands: calibration, vectors, overdue, export")
    else:
        tracker.print_status_report()
        tracker.print_calibration_report()


if __name__ == '__main__':
    main()
