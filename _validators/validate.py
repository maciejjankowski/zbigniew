#!/usr/bin/env python3
"""
ZBIGNIEW Protocol Validator

Validates data integrity across the framework:
- JSON schema validation for predictions, events
- Confidence level calibration checks
- Cross-reference validation (sources exist)
- Prediction deadline tracking
"""

import json
import sys
from datetime import datetime, date
from pathlib import Path
from typing import Any

# Optional: jsonschema for full validation
try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

# Confidence level to probability mapping
CONFIDENCE_RANGES = {
    1: (1, 25),    # Very Low: 1-25%
    2: (25, 50),   # Low: 25-50%
    3: (50, 75),   # Medium: 50-75%
    4: (75, 90),   # High: 75-90%
    5: (90, 99),   # Very High: 90-99%
}

VALID_VECTORS = [
    "INSTITUTIONAL", "ALLIANCE", "ECONOMIC",
    "INFORMATION", "MILITARY", "POLITICAL", "SOCIAL"
]

VALID_CATEGORIES = [
    "policy", "military", "economic", "diplomatic",
    "domestic", "social", "institutional"
]

VALID_STATUSES = ["active", "confirmed", "refuted", "expired", "partial"]


class ValidationResult:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    def add_info(self, msg: str):
        self.info.append(msg)

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0

    def print_report(self):
        if self.errors:
            print("\n\033[91m=== ERRORS ===\033[0m")
            for e in self.errors:
                print(f"  \033[91m✗\033[0m {e}")

        if self.warnings:
            print("\n\033[93m=== WARNINGS ===\033[0m")
            for w in self.warnings:
                print(f"  \033[93m⚠\033[0m {w}")

        if self.info:
            print("\n\033[94m=== INFO ===\033[0m")
            for i in self.info:
                print(f"  \033[94mℹ\033[0m {i}")

        print()
        if self.passed:
            print("\033[92m✓ Validation PASSED\033[0m")
        else:
            print(f"\033[91m✗ Validation FAILED ({len(self.errors)} errors)\033[0m")


def load_jsonl(path: Path) -> list[dict]:
    """Load JSONL file, skipping schema header lines."""
    entries = []
    with open(path, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                # Skip schema/header lines
                if obj.get('_schema') or obj.get('_version'):
                    continue
                obj['_line'] = line_num
                entries.append(obj)
            except json.JSONDecodeError as e:
                print(f"JSON error line {line_num}: {e}")
    return entries


def validate_prediction(pred: dict, result: ValidationResult, sources: set[str]):
    """Validate a single prediction entry."""
    line = pred.get('_line', '?')
    pred_id = pred.get('id', 'UNKNOWN')

    # Required fields
    required = ['id', 'prediction', 'deadline', 'confidence', 'confidence_pct',
                'category', 'vectors', 'falsification', 'status']
    for field in required:
        if field not in pred:
            result.error(f"[{pred_id}] Missing required field: {field}")

    # ID format
    if 'id' in pred and not pred['id'].startswith('pred_'):
        result.error(f"[{pred_id}] Invalid ID format (should be pred_YYYY_NNN)")

    # Confidence calibration
    if 'confidence' in pred and 'confidence_pct' in pred:
        conf = pred['confidence']
        pct = pred['confidence_pct']
        if conf in CONFIDENCE_RANGES:
            low, high = CONFIDENCE_RANGES[conf]
            if not (low <= pct <= high):
                result.warn(f"[{pred_id}] Confidence {conf} suggests {low}-{high}%, but stated {pct}%")
        else:
            result.error(f"[{pred_id}] Invalid confidence level: {conf} (must be 1-5)")

    # Category validation
    if 'category' in pred and pred['category'] not in VALID_CATEGORIES:
        result.error(f"[{pred_id}] Invalid category: {pred['category']}")

    # Vectors validation
    if 'vectors' in pred:
        for v in pred['vectors']:
            if v not in VALID_VECTORS:
                result.error(f"[{pred_id}] Invalid vector: {v}")

    # Status validation
    if 'status' in pred and pred['status'] not in VALID_STATUSES:
        result.error(f"[{pred_id}] Invalid status: {pred['status']}")

    # Deadline check
    if 'deadline' in pred:
        try:
            deadline = datetime.strptime(pred['deadline'], '%Y-%m-%d').date()
            days_until = (deadline - date.today()).days
            if days_until < 0 and pred.get('status') == 'active':
                result.warn(f"[{pred_id}] Deadline PASSED ({pred['deadline']}) but status still 'active'")
            elif 0 <= days_until <= 30:
                result.add_info(f"[{pred_id}] Deadline in {days_until} days ({pred['deadline']})")
        except ValueError:
            result.error(f"[{pred_id}] Invalid deadline format: {pred['deadline']}")

    # Falsification criteria length
    if 'falsification' in pred and len(pred['falsification']) < 20:
        result.warn(f"[{pred_id}] Falsification criteria too short (be specific)")


def validate_event(event: dict, result: ValidationResult, sources: set[str]):
    """Validate a single event entry."""
    event_id = event.get('id', 'UNKNOWN')

    # Required fields
    required = ['id', 'date', 'title', 'description', 'category', 'confidence']
    for field in required:
        if field not in event:
            result.error(f"[{event_id}] Missing required field: {field}")

    # ID format
    if 'id' in event and not event['id'].startswith('evt_'):
        result.error(f"[{event_id}] Invalid ID format (should be evt_YYYY_...)")

    # Source cross-reference
    if 'sources' in event:
        for src_id in event['sources']:
            if src_id not in sources:
                result.warn(f"[{event_id}] Source not found in index: {src_id}")

    # Vectors validation
    if 'vectors' in event:
        for v in event['vectors']:
            if v not in VALID_VECTORS:
                result.error(f"[{event_id}] Invalid vector: {v}")

    # Confidence range
    if 'confidence' in event:
        if not (1 <= event['confidence'] <= 5):
            result.error(f"[{event_id}] Invalid confidence: {event['confidence']} (must be 1-5)")


def load_source_ids(base_path: Path) -> set[str]:
    """Extract source IDs from index.yaml."""
    source_ids = set()
    yaml_path = base_path / '_sources' / 'index.yaml'

    if not yaml_path.exists():
        return source_ids

    # Simple extraction without full YAML parsing
    with open(yaml_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('- id:'):
                src_id = line.replace('- id:', '').strip().strip('"\'')
                source_ids.add(src_id)

    return source_ids


def validate_all(base_path: Path) -> ValidationResult:
    """Run all validations."""
    result = ValidationResult()

    # Load source IDs for cross-reference
    sources = load_source_ids(base_path)
    result.add_info(f"Loaded {len(sources)} source IDs from index")

    # Validate predictions
    pred_path = base_path / '_predictions' / 'active.jsonl'
    if pred_path.exists():
        predictions = load_jsonl(pred_path)
        result.add_info(f"Validating {len(predictions)} predictions")
        for pred in predictions:
            validate_prediction(pred, result, sources)
    else:
        result.warn("Predictions file not found")

    # Validate events
    events_path = base_path / '_timeline' / 'events.jsonl'
    if events_path.exists():
        events = load_jsonl(events_path)
        result.add_info(f"Validating {len(events)} events")
        for event in events:
            validate_event(event, result, sources)
    else:
        result.warn("Events file not found")

    return result


def main():
    # Find base path
    script_dir = Path(__file__).parent
    base_path = script_dir.parent

    print("=" * 50)
    print("ZBIGNIEW Protocol Validator")
    print("=" * 50)
    print(f"Base path: {base_path}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 50)

    result = validate_all(base_path)
    result.print_report()

    sys.exit(0 if result.passed else 1)


if __name__ == '__main__':
    main()
