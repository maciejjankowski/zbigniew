# REASONING IMPROVEMENTS

*Six upgrades to strengthen Zbigniew assessments. Identified 2026-02-20 after SAFE assessment (asmt_2026_004) field-testing.*

---

## 1. STEEL-MAN THE OPPOSITION

*Don't just Red Team your thesis. Build the best possible case against it.*

### The Problem

Current Red Team sections often construct weak counter-arguments, then defeat them. This is intellectual theater, not adversarial testing. The SAFE assessment argues Poland is being exploited — but never fully constructs the case that SAFE *genuinely* builds Polish industrial capacity.

### The Standard

Before finalizing any Key Judgment, write a **"Strongest Case Against"** section:

1. Assume good faith from the opposing position
2. Use their best evidence, not your characterization of it
3. Identify where their argument is genuinely strong
4. Show *specifically* where it breaks — with evidence, not assertion

### Template

```markdown
## Strongest Case Against Judgment N

**The opposing position:** [State it as its proponents would]

**Their best evidence:**
1. [Strongest supporting fact]
2. [Second strongest]
3. [Third]

**Where this argument is genuinely strong:**
[Acknowledge the valid parts honestly]

**Where it breaks — specifically:**
1. [Fact/logic that undermines it] — Source: [citation]
2. [Fact/logic that undermines it] — Source: [citation]

**Net assessment:** [How this affects our confidence level]
```

### Example (SAFE)

**Opposing position:** SAFE builds Polish defence industrial capacity through EU-funded procurement, creating jobs and technology transfer.

**Their best evidence:**
1. PGZ has announced expansion plans tied to SAFE funding
2. EU content rules allow Polish subcontracting within European primes
3. Poland's defence budget was already straining before SAFE

**Where genuinely strong:** Poland *does* need the investment, and some technology transfer *will* occur through subcontracting arrangements.

**Where it breaks:**
1. 65% EU content ≠ 65% Polish content. French/German primes satisfy the rule while subcontracting 10-20% to Polish firms — Source: EU Regulation 2024/xxx, Art. 12
2. No additionality clause means SAFE can *replace* domestic spending — Source: regulation text comparison with NGEU additionality requirements
3. PGZ's stated expansion plans assume contracts that aren't guaranteed by the regulation

---

## 2. QUANTITATIVE RANGES

*Replace "MODERATE confidence" with numbers people can reason about.*

### The Problem

"Poland will likely see 25-40% domestic content" communicates more than "MODERATE confidence that a significant portion will go abroad." Qualitative labels hide the reasoning.

### The Standard

Every claim involving quantities must include:

```markdown
**Claim:** [Statement]
**Range:** [Low estimate] — [Base case] — [High estimate]
**Assumptions:**
  - Low: [What would have to be true]
  - Base: [Most likely scenario]
  - High: [What would have to be true]
**Government claim:** [If different, state it]
**Gap explained by:** [Why estimates differ]
```

### Rules

1. **Always state assumptions.** A number without assumptions is a guess.
2. **Always show the range.** Single-point estimates create false precision.
3. **Always note when government/official numbers differ** and explain the gap.
4. **Never present inferred numbers as confirmed.** "~€28B" is inference from 65% × €43.7B. Label it.

### When Quantitative Data Isn't Available

Say so explicitly:

```markdown
**Claim:** Most SAFE funds will go to non-Polish European producers
**Quantification:** Not possible with public data
**Bounds:** 65% EU content floor (regulation), 80-90% Polish claim (Sobkowiak-Czarnecka, no source provided)
**What would resolve this:** PGZ capacity audits, historical EU content enforcement data from NGEU
```

---

## 3. PREDICTION TRACKING & SIGNAL WATCH

*Predictions without review cadence are just opinions with deadlines.*

### The Problem

`active.jsonl` has 14 predictions. None have been reviewed since creation. There's no system for tracking intermediate signals.

### The Standard

Each prediction gets a **Signal Watch** — observable events that would move confidence up or down *before* the deadline.

```jsonl
{
  "id": "pred_2026_015",
  "prediction": "...",
  "deadline": "2027-06-30",
  "confidence": 3,
  "signal_watch": {
    "confidence_up": [
      {"signal": "PGZ announces facility closure or reduced headcount", "weight": "+0.5"},
      {"signal": "EU Commission rejects Polish procurement plan", "weight": "+1.0"}
    ],
    "confidence_down": [
      {"signal": "Rheinmetall opens manufacturing plant in Poland", "weight": "-0.5"},
      {"signal": "Poland negotiates EU content waiver for domestic systems", "weight": "-1.0"}
    ]
  },
  "review_cadence": "monthly",
  "last_reviewed": null
}
```

### Review Protocol

1. **Monthly:** Scan signal watch items. Any triggered? Update confidence.
2. **Quarterly:** Full prediction review. Mark resolved, update active.
3. **On major event:** Immediate review of affected predictions.
4. **Log every update** in `_predictions/review_log.jsonl`:

```jsonl
{"date": "2026-03-15", "prediction_id": "pred_2026_015", "trigger": "Rheinmetall Poland expansion announced", "old_confidence": 3, "new_confidence": 2, "rationale": "Counter-signal to our thesis — indicates some domestic benefit"}
```

---

## 4. SOURCE DIVERSITY REQUIREMENTS

*If all your sources agree with you, you're reading the wrong sources.*

### The Problem

The SAFE assessment relies predominantly on English-language Western analysis. For a Polish defence procurement assessment, this creates a structural blind spot.

### The Standard

**Minimum Source Diversity per Assessment:**

| Requirement | Minimum | Purpose |
|-------------|---------|---------|
| Languages | 2+ | Avoid anglophone bias |
| Government primary sources | Both sides | Not just the side you're critiquing |
| Source hostile to your thesis | 1+ | Force engagement with counter-evidence |
| Institutional analysis | 2+ think tanks | Cross-check analytical frames |
| Domain-specific | 1+ industry source | Ground truth from practitioners |

### Source Diversity Checklist

```markdown
## Source Audit: [Assessment ID]

### Language Coverage
- [ ] English sources: [count]
- [ ] Polish sources: [count]
- [ ] Other languages: [list]
- [ ] Government docs in original language: [Y/N]

### Perspective Coverage
- [ ] Sources supporting thesis: [count]
- [ ] Sources opposing thesis: [count]
- [ ] Neutral/analytical sources: [count]

### Source Type Coverage
- [ ] Government primary docs: [count]
- [ ] Think tank analysis: [count]
- [ ] Journalism: [count]
- [ ] Industry/practitioner: [count]
- [ ] Academic: [count]

### Gaps Identified
- [ ] [List missing perspectives]
- [ ] [List missing source types]
- [ ] Impact on confidence: [assessment]
```

### For SAFE Specifically — Missing Sources

| Source Type | Examples | Why Needed |
|-------------|----------|------------|
| Polish MOD | Procurement plans, force modernization | Government's own reasoning |
| PGZ reports | Annual reports, capacity data | Ground truth on Polish capability |
| PISM/OSW | Polish think tank analysis | Polish analytical perspective |
| NIK audits | Supreme Audit Office | Historical compliance data |
| Rheinmetall IR | Investor relations, annual report | Supplier perspective |
| BMVg | German defence ministry | German government position |
| SWP | German think tank | German analytical perspective |
| NGEU implementation reports | EU Commission | Historical precedent data |

---

## 5. BASE RATE COMPARISON

*Every instrument has predecessors. Check what actually happened.*

### The Problem

The SAFE assessment treats the instrument as novel. But the EU has run large conditional lending programs before — Recovery Fund, NGEU, structural funds, Greek bailouts. What *actually* happened with content rules, conditionality, and domestic industry capture?

### The Standard

Every assessment involving a financial instrument, policy mechanism, or institutional action must include:

```markdown
## Historical Parallel

**Instrument:** [Current instrument]
**Closest precedent:** [Historical instrument]

### What Was Promised
[Official claims at launch]

### What Actually Happened
[Documented outcomes, with sources]

### Structural Similarities
1. [Same feature] — likely same outcome because [reasoning]
2. [Same feature] — likely same outcome because [reasoning]

### Structural Differences
1. [Different feature] — outcome may differ because [reasoning]
2. [Different feature] — outcome may differ because [reasoning]

### Net Assessment
Based on precedent, [prediction] with [confidence level]
```

### Key Questions

1. **Were content/procurement rules enforced?** Check EU implementation reports.
2. **Did domestic industry actually benefit?** Check employment, revenue data post-instrument.
3. **Was conditionality exercised?** Check if Rule of Law mechanism was ever triggered on comparable instruments.
4. **Did "additionality" hold?** Check if domestic spending was maintained or substituted.

---

## 6. ASSESSMENT VERSIONING & LIVING DOCUMENTS

*An assessment is a snapshot. Reality keeps moving.*

### The Problem

Assessments are published as static documents. New evidence (Tusk bypassing veto, WB GROUP counter-narrative, new domestic defence systems) doesn't update the original. Readers get a frozen analysis in a moving world.

### The Standard

Every published assessment gets a **Signals Since Publication** appendix that logs new evidence without rewriting the original.

### Structure

```markdown
## Signals Since Publication

*Assessment version: 1.0 (2026-02-20)*
*Last signal update: 2026-02-20*

### Signal Log

| Date | Signal | Direction | Impact | Source |
|------|--------|-----------|--------|--------|
| 2026-02-20 | Tusk: will proceed with SAFE despite potential presidential veto | Neutral (political, not structural) | Does not change financial terms | Brussels Signal |
| 2026-02-20 | WB GROUP/Darowska on TVP: "SAFE is investment, not loan" | Counter | Official narrative hardening; no new evidence provided | WB GROUP LinkedIn |
| 2026-02-18 | SA-35MM by PIT-RADWAR unveiled — 100% domestic content | Supporting | Proves Polish capability exists without SAFE | Samir Khayat / defence press |

### Net Effect on Key Judgments

| Judgment | Original Confidence | Current Confidence | Change Reason |
|----------|--------------------|--------------------|---------------|
| KJ-1 | MODERATE | MODERATE | No change — new signals balance |
| KJ-2 | MODERATE-HIGH | MODERATE-HIGH | SA-35MM supports domestic capability thesis |

### Assessment Status: CURRENT (no revision needed)
```

### Versioning Rules

1. **v1.0:** Original publication
2. **Signal updates:** Don't change version, just append to log
3. **v1.1:** Minor revision (new evidence changes confidence on 1-2 judgments)
4. **v2.0:** Major revision (structural change to thesis, new key judgments)
5. **SUPERSEDED:** New assessment replaces this one entirely

### Automation

Track signals via `_predictions/signal_watch` items. When a signal fires, prompt:
1. Does this affect any active assessment?
2. If yes, add to that assessment's signal log
3. If confidence changes ≥1 level, flag for revision

---

## INTEGRATION

These six improvements are additive — they don't replace existing methodology docs. They extend:

| Existing Doc | Extended By |
|-------------|------------|
| `confidence_levels.md` | §2 Quantitative Ranges |
| `cui_bono.md` | §1 Steel-Manning (stronger adversary test) |
| `validation_gate.md` | §4 Source Diversity (new checklist) |
| `source_verification.md` | §4 Source Diversity + §5 Base Rate |
| `pattern_mapping.md` | §5 Base Rate Comparison |
| (new) | §3 Signal Watch, §6 Versioning |

---

## ORIGIN

Identified during field-testing of `asmt_2026_004_safe_program`:
- Steel-manning gap: WB GROUP/Darowska counter-narrative not fully addressed
- Quantitative gap: "~€28B" presented without range or assumptions
- Prediction gap: 9 SAFE predictions not in tracking system
- Source gap: Zero Polish-language sources in an assessment about Poland
- Base rate gap: No comparison to NGEU or Recovery Fund outcomes
- Versioning gap: Three new data points found same day, no mechanism to integrate

*por. Zbigniew / Pattern recognition, not prophecy*
