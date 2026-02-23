# ZBIGNIEW PROTOCOL

**Open-Source Political Intelligence Analysis Framework**

*Pattern recognition, not prophecy. Verified sources only.*

---

## WHAT THIS IS

A systematic methodology for analyzing political events, policy decisions, and geopolitical patterns using only open-source intelligence (OSINT). Designed for:

1. **Thinking** - Rigorous analytical methodology
2. **Publishing** - Accessible intelligence assessments
3. **Recordkeeping** - Timestamped timelines and predictions

---

## CORE PRINCIPLES

```
1. VERIFIED SOURCES ONLY
   - Primary documents (official transcripts, government publications)
   - Established journalism (with direct quotes/documents)
   - Academic analysis (peer-reviewed or institutional)
   - NO speculation presented as fact
   - NO anonymous sourcing without corroboration

2. CUI BONO (WHO BENEFITS)
   - Every policy has beneficiaries
   - Map actions to outcomes
   - Follow the incentives, not the rhetoric
   - Ask: "If an adversary designed this policy, what would differ?"

3. PATTERN RECOGNITION
   - Individual events are noise
   - Patterns across vectors are signal
   - Document the pattern, let readers conclude

4. FALSIFIABILITY
   - State what would prove the analysis wrong
   - Include confidence levels
   - Update when evidence changes

5. TIMESTAMP EVERYTHING
   - Assessments are dated
   - Predictions have deadlines
   - Revisions are tracked, never hidden
```

---

## DIRECTORY STRUCTURE

```
zbigniew-protocol/
├── CLAUDE.md                 # This file - framework entry point
├── README.md                 # Public-facing description
│
├── _methodology/             # HOW TO THINK
│   ├── cui_bono.md          # Beneficiary analysis + money flow tracing + TCO + counter-narratives
│   ├── pattern_mapping.md   # Cross-vector recognition + named patterns (demand-side subsidy, core-periphery, etc.)
│   ├── source_verification.md # Source hierarchy and validation
│   ├── confidence_levels.md # Assessment confidence system
│   ├── cognitive_biases.md  # 12 biases + Sagan foundation + pre-analysis/publication checklists
│   ├── actor_background_checks.md # Personnel file methodology — track records, conflicts, Bad Apples Matrix
│   ├── reasoning_improvements.md  # 6 structural upgrades (steel-man, quantitative ranges, signal watch, source diversity, base rate, versioning)
│   ├── red_team.md          # Adversarial self-critique
│   └── persona_stability.md # AI analytical frame maintenance
│
├── _assessments/             # INTELLIGENCE PRODUCTS
│   ├── active/              # Current assessments
│   ├── archived/            # Historical assessments
│   └── templates/           # Assessment templates
│
├── _timeline/                # EVENT TRACKING
│   ├── events.jsonl         # Timestamped event log
│   ├── policies.jsonl       # Policy changes
│   ├── statements.jsonl     # Official statements
│   └── by_year/             # Annual timeline summaries
│
├── _sources/                 # SOURCE LIBRARY
│   ├── primary/             # Government docs, official transcripts
│   ├── analysis/            # Think tank, academic sources
│   └── index.yaml           # Source index with reliability ratings
│
├── _predictions/             # TRACKED PREDICTIONS
│   ├── active.jsonl         # Open predictions
│   ├── resolved.jsonl       # Confirmed/refuted predictions
│   └── accuracy.md          # Prediction track record
│
├── _publishing/              # OUTPUT FORMATS
│   ├── templates/           # Article, brief, assessment templates
│   ├── style_guide.md       # Writing standards
│   └── distribution.md      # Publishing channels
│
├── _memory/                  # DECISION LOG
│   ├── assessments.jsonl    # Assessment decisions and reasoning
│   └── revisions.jsonl      # When and why assessments changed
│
└── _tools/                   # ANALYSIS UTILITIES
    ├── timeline_generator.py
    ├── source_checker.py
    └── prediction_tracker.py
```

---

## ASSESSMENT WORKFLOW

### Phase 1: OBSERVE
- Collect events, statements, policies
- Log to `_timeline/` with timestamps
- Note source for each item

### Phase 2: PATTERN
- Map events across vectors (institutional, alliance, economic, etc.)
- Identify beneficiaries for each action
- Look for coordinated vs. coincidental patterns

### Phase 3: ANALYZE
- Apply cui bono framework
- Check against documented strategies (e.g., Russia's NSS 2021)
- Rate confidence level
- Identify what would falsify the analysis

### Phase 4: PUBLISH
- Select format (brief, full assessment, addendum)
- Apply style guide
- Include sources, confidence, falsifiability
- Timestamp

### Phase 5: TRACK
- Log predictions with deadlines
- Update when new evidence emerges
- Maintain accuracy record

---

## CONFIDENCE LEVELS

| Level | Label | Meaning |
|-------|-------|---------|
| 5 | CONFIRMED | Primary source documentation |
| 4 | HIGH | Multiple reliable sources agree |
| 3 | MODERATE | Logical inference from confirmed facts |
| 2 | LOW | Single source or circumstantial |
| 1 | SPECULATIVE | Pattern suggests but evidence thin |

**Rule**: Never present Level 1-2 as fact. Always label.

---

## VECTOR CATEGORIES

Standard vectors for cross-domain analysis:

1. **INSTITUTIONAL** - Government capacity, agency independence, civil service
2. **ALLIANCE** - NATO, EU, bilateral relationships, treaty obligations
3. **ECONOMIC** - Sanctions, trade, currency, debt
4. **INFORMATION** - Media, propaganda, platform control, censorship
5. **MILITARY** - Posture, deployments, readiness, doctrine
6. **POLITICAL** - Domestic polarization, elections, rule of law
7. **SOCIAL** - Civil unrest, migration, public trust

---

## COGNITIVE BIAS CHECKLIST

Before finalizing any assessment, check for:

- [ ] **Confirmation bias** - Am I seeking evidence that confirms my hypothesis?
- [ ] **Anchoring** - Am I over-weighting early information?
- [ ] **Attribution error** - Am I assuming intent from outcome?
- [ ] **Availability heuristic** - Am I over-weighting recent/memorable events?
- [ ] **Mirror imaging** - Am I assuming adversaries think like me?
- [ ] **Groupthink** - Am I conforming to consensus without evidence?
- [ ] **Persona drift** - Have I maintained analytical distance throughout?
- [ ] **Emotional entanglement** - Am I analyzing or validating the user?

---

## RED TEAM QUESTIONS

Before publishing, answer:

1. What's the strongest argument AGAINST this assessment?
2. What alternative explanation fits the same facts?
3. What would a defender of the subject say?
4. What am I missing that would change my conclusion?
5. In 2 years, what might make this assessment look foolish?
6. Am I telling the user what they want to hear? (persona stability check)
7. Would my analysis differ if the user had opposite beliefs?
8. Have I maintained the same evidentiary standards throughout?

---

## QUICK START

1. **New Event**: Log to `_timeline/events.jsonl`
2. **New Assessment**: Copy template from `_assessments/templates/`
3. **New Prediction**: Add to `_predictions/active.jsonl`
4. **Update Assessment**: Log revision to `_memory/revisions.jsonl`
5. **Publish**: Use templates in `_publishing/templates/`

---

## REMEMBER

> "The question is not 'who is an asset' (attribution problem).
> The question is: 'Why does this policy portfolio perfectly match
> the wish-list of adversaries?'"

Pattern recognition, not prophecy.
Verified sources only.
Timestamp everything.
