# PREDICTION TRACKING SYSTEM

*Accountability through tracked predictions. Hubris dies in sunlight.*

---

## WHY TRACK PREDICTIONS

1. **Accountability** - Forces intellectual honesty
2. **Calibration** - Learn your biases over time
3. **Credibility** - Track record speaks for itself
4. **Methodology improvement** - What works? What doesn't?

---

## FILES

```
_predictions/
├── active.jsonl      # Open predictions awaiting resolution
├── resolved.jsonl    # Confirmed or refuted predictions
└── accuracy.md       # Running accuracy statistics
```

---

## PREDICTION SCHEMA

```json
{
  "id": "pred_2026_001",
  "created": "2026-01-20T12:00:00Z",
  "assessment_ref": "asmt_2026_001",
  "prediction": "Clear statement of what will happen",
  "timeframe": "By 2026-06-30",
  "deadline": "2026-06-30",
  "confidence": 3,
  "confidence_pct": 65,
  "category": "policy|military|economic|diplomatic|domestic",
  "vectors": ["ALLIANCE", "INSTITUTIONAL"],
  "falsification": "What would prove this wrong",
  "status": "active|confirmed|refuted|expired|revised",
  "resolution_date": null,
  "resolution_notes": null,
  "sources_at_prediction": ["src_2026_001"]
}
```

---

## PREDICTION RULES

### Rule 1: Be Specific
- Bad: "Things will get worse"
- Good: "NATO Article 5 invocation will not occur for Greenland by Q2 2026"

### Rule 2: Set Deadlines
- Every prediction has a timeframe
- Open-ended predictions are not predictions

### Rule 3: State Confidence as Probability
- "I'm 70% confident" not "I think maybe"
- Use percentage for calibration tracking

### Rule 4: Define Falsification
- What specific outcome would prove you wrong?
- If nothing would, it's not a real prediction

### Rule 5: Record Immediately
- Predictions made at time of assessment
- No backdating

---

## RESOLUTION PROCESS

When deadline arrives:

1. **Assess outcome** - What actually happened?
2. **Compare to prediction** - Match, partial, miss?
3. **Move to resolved.jsonl** - With resolution notes
4. **Update accuracy.md** - Running statistics
5. **Extract learnings** - What did you miss? Why?

---

## ACCURACY TRACKING

Maintain running statistics:

```markdown
## Prediction Accuracy (Updated: YYYY-MM-DD)

### Overall
- Total predictions: N
- Confirmed: N (X%)
- Refuted: N (X%)
- Expired: N (X%)

### By Confidence Level
| Confidence | Predicted | Confirmed | Accuracy |
|------------|-----------|-----------|----------|
| 5 (90%+) | N | N | X% |
| 4 (75-90%) | N | N | X% |
| 3 (50-75%) | N | N | X% |
| 2 (25-50%) | N | N | X% |
| 1 (<25%) | N | N | X% |

### By Category
| Category | Predictions | Accuracy |
|----------|-------------|----------|
| Policy | N | X% |
| Military | N | X% |
| Economic | N | X% |

### Calibration Analysis
[Are 70% confidence predictions right 70% of the time?]
```

---

## EXAMPLE PREDICTION

```json
{
  "id": "pred_2026_001",
  "created": "2026-01-20T12:00:00Z",
  "assessment_ref": "asmt_2026_001",
  "prediction": "At least one additional NATO ally will face explicit territorial pressure (beyond Denmark/Greenland) by end of Q1 2026",
  "timeframe": "By 2026-03-31",
  "deadline": "2026-03-31",
  "confidence": 4,
  "confidence_pct": 80,
  "category": "diplomatic",
  "vectors": ["ALLIANCE"],
  "falsification": "No additional NATO territory faces public US pressure or threat by deadline",
  "status": "active",
  "resolution_date": null,
  "resolution_notes": null,
  "sources_at_prediction": ["src_2026_001", "src_2026_003"]
}
```

---

## RESOLUTION EXAMPLE

```json
{
  "id": "pred_2026_001",
  "created": "2026-01-20T12:00:00Z",
  "prediction": "At least one additional NATO ally will face explicit territorial pressure...",
  "deadline": "2026-03-31",
  "confidence_pct": 80,
  "status": "confirmed",
  "resolution_date": "2026-02-15",
  "resolution_notes": "Canada faced explicit annexation rhetoric on 2026-02-10. Prediction confirmed 6 weeks before deadline.",
  "actual_outcome": "Canada territorial pressure via tariffs and annexation rhetoric",
  "accuracy_assessment": "Prediction confirmed. Pattern recognition of escalation was accurate."
}
```

---

## CALIBRATION GOAL

Well-calibrated predictions:
- 90% confidence predictions: right ~90% of the time
- 70% confidence predictions: right ~70% of the time
- 50% confidence predictions: right ~50% of the time

If your 70% predictions are right 95% of the time, you're underconfident.
If your 70% predictions are right 40% of the time, you're overconfident.

Track and adjust.
