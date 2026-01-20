# TIMELINE SYSTEM

*Timestamp everything. History is written by those who document.*

---

## STRUCTURE

```
_timeline/
├── events.jsonl        # All significant events
├── policies.jsonl      # Policy changes and decisions
├── statements.jsonl    # Official statements (quotes)
├── predictions.jsonl   # Predictions made (linked to _predictions/)
└── by_year/
    ├── 2025.md        # Annual summary
    └── 2026.md        # Annual summary
```

---

## EVENT SCHEMA

Each event in `events.jsonl`:

```json
{
  "id": "evt_2026_0120_001",
  "timestamp": "2026-01-20T12:00:00Z",
  "date": "2026-01-20",
  "title": "Short descriptive title",
  "description": "Detailed description of what happened",
  "category": "policy|statement|action|personnel|military|economic|diplomatic",
  "vectors": ["INSTITUTIONAL", "ALLIANCE"],
  "actors": ["Entity1", "Entity2"],
  "beneficiaries": ["Entity1"],
  "sources": ["src_2026_001", "src_2026_002"],
  "confidence": 5,
  "tags": ["nato", "tariffs", "trade"],
  "related_events": ["evt_2026_0115_003"],
  "assessment_refs": ["asmt_2026_001"]
}
```

---

## POLICY SCHEMA

Each policy in `policies.jsonl`:

```json
{
  "id": "pol_2026_001",
  "timestamp": "2026-01-20T00:00:00Z",
  "date": "2026-01-20",
  "title": "Policy name/executive order/legislation",
  "type": "executive_order|legislation|regulation|directive|treaty",
  "authority": "Who enacted it",
  "stated_rationale": "Official justification",
  "actual_effects": ["Effect 1", "Effect 2"],
  "beneficiaries": {
    "domestic": ["Entity1"],
    "foreign": ["Entity2"],
    "institutional": ["Entity3"]
  },
  "vectors_affected": ["INSTITUTIONAL", "ALLIANCE"],
  "sources": ["src_2026_001"],
  "confidence": 4,
  "cui_bono_ref": "cuibono_2026_001"
}
```

---

## STATEMENT SCHEMA

Each statement in `statements.jsonl`:

```json
{
  "id": "stmt_2026_001",
  "timestamp": "2026-01-20T15:30:00Z",
  "date": "2026-01-20",
  "speaker": "Person or entity",
  "role": "Position/title at time",
  "quote": "Exact quote text",
  "context": "Where/when said, surrounding context",
  "significance": "Why this matters",
  "sources": ["src_2026_001"],
  "verified": true,
  "related_events": ["evt_2026_0120_001"]
}
```

---

## USAGE

### Adding an Event

```bash
# Use the timeline tool (or manually append)
python _tools/timeline_generator.py add-event \
  --date "2026-01-20" \
  --title "NATO ally tariffs announced" \
  --category policy \
  --vectors ALLIANCE,ECONOMIC \
  --sources src_2026_001
```

### Querying Timeline

```bash
# Events by date range
python _tools/timeline_generator.py query \
  --start "2026-01-01" \
  --end "2026-01-31" \
  --category policy

# Events by vector
python _tools/timeline_generator.py query \
  --vector ALLIANCE

# Events by beneficiary
python _tools/timeline_generator.py query \
  --beneficiary Russia
```

### Generating Annual Summary

```bash
python _tools/timeline_generator.py summarize \
  --year 2026 \
  --output _timeline/by_year/2026.md
```

---

## ID CONVENTIONS

- Events: `evt_YYYY_MMDD_NNN` (e.g., `evt_2026_0120_001`)
- Policies: `pol_YYYY_NNN` (e.g., `pol_2026_001`)
- Statements: `stmt_YYYY_NNN` (e.g., `stmt_2026_001`)
- Sources: `src_YYYY_NNN` (e.g., `src_2026_001`)
- Assessments: `asmt_YYYY_NNN` (e.g., `asmt_2026_001`)

---

## BEST PRACTICES

1. **Log immediately** - Don't let events pile up
2. **Be specific** - Dates, times, exact quotes
3. **Source everything** - No orphan claims
4. **Link related items** - Build the graph
5. **Review regularly** - Patterns emerge over time
