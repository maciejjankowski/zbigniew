# VALIDATION GATE

**CRITICAL: NO HALLUCINATED CONTENT**

*Every piece of data must pass this gate before entering the framework.*

---

## THE IRON RULE

```
IF no_source THEN reject
IF source_not_verifiable THEN reject
IF claim_exceeds_source THEN reject
```

---

## VALIDATION CHECKLIST

Before ANY data enters `_timeline/`, `_assessments/`, or `_predictions/`:

### 1. SOURCE EXISTS
- [ ] Claim has explicit source citation
- [ ] Source URL is provided
- [ ] Source is accessible (or archived)

### 2. SOURCE SUPPORTS CLAIM
- [ ] Source actually says what is claimed
- [ ] Quote is exact (not paraphrased beyond recognition)
- [ ] Context is preserved (not cherry-picked)

### 3. CLAIM DOESN'T EXCEED SOURCE
- [ ] Claim is not stronger than source supports
- [ ] Inference is labeled as inference
- [ ] Speculation is labeled as speculation

### 4. NO HALLUCINATION
- [ ] Dates are from source, not assumed
- [ ] Numbers are from source, not estimated
- [ ] Names/entities are from source, not filled in
- [ ] Events actually happened (not projected)

---

## DATA IMPORT PROTOCOL

When importing from existing content:

### Step 1: Extract Only Sourced Claims
```
For each claim in article:
  IF has_source_link:
    EXTRACT claim + source
  ELSE:
    SKIP (do not import)
```

### Step 2: Verify Source Still Says This
```
For each extracted claim:
  FETCH source
  VERIFY claim matches source
  IF mismatch: FLAG for review
```

### Step 3: Categorize Confidence
```
PRIMARY_SOURCE (gov docs, transcripts) → Confidence 5
INSTITUTIONAL (think tanks, academic) → Confidence 4
JOURNALISM (with documents/quotes) → Confidence 3-4
SINGLE_SOURCE → Confidence 2
NO_CLEAR_SOURCE → REJECT
```

### Step 4: Flag Inferences
```
IF claim is INFERENCE from source (not direct quote):
  LABEL as inference
  REDUCE confidence by 1 level
  NOTE the logical step taken
```

---

## RED FLAGS - REJECT IMMEDIATELY

1. **"According to reports..."** - Which reports? Reject until specified.
2. **Round numbers without source** - "50,000 workers" needs citation
3. **Dates without source** - "On January 15..." needs verification
4. **Causal claims** - "X caused Y" needs evidence of causation
5. **Intent claims** - "They intended to..." needs evidence of intent
6. **Future predictions as fact** - Predictions go to `_predictions/`, not timeline

---

## VALIDATION LOG

Every import session must log:

```yaml
import_session:
  date: YYYY-MM-DD
  source_article: "filename"
  claims_extracted: N
  claims_verified: N
  claims_rejected: N
  rejection_reasons:
    - claim: "..."
      reason: "no source"
    - claim: "..."
      reason: "source doesn't support"
```

---

## EXAMPLE: VALID vs INVALID

### VALID IMPORT
```
Claim: "Russia's 2021 NSS designates the US as an 'unfriendly state'"
Source: Carnegie Endowment analysis + Original Russian document
Verification: Direct quote in source ✓
Confidence: 5 (primary document)
→ IMPORT
```

### INVALID IMPORT
```
Claim: "271,000 federal workers removed"
Source: None provided in article
Verification: Cannot verify
→ REJECT until source provided
```

### BORDERLINE - NEEDS FLAGGING
```
Claim: "This benefits Russia"
Source: Pattern analysis (not direct source)
Verification: Inference, not direct evidence
→ IMPORT as INFERENCE with Confidence 3, flag as analytical judgment
```

---

## REMEMBER

> "Better to have a sparse timeline with verified data
> than a complete timeline with hallucinated garbage."

When in doubt, **DON'T IMPORT**.
Flag for later verification.
Empty fields are better than wrong fields.
