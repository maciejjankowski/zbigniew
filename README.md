# ZBIGNIEW PROTOCOL

**Open-Source Political Intelligence Analysis Framework**

*Pattern recognition, not prophecy. Verified sources only.*

---

## What Is This?

A systematic methodology for analyzing political events, policy decisions, and geopolitical patterns using only open-source intelligence (OSINT).

Designed for:
- **Thinking** - Rigorous analytical methodology
- **Publishing** - Accessible intelligence assessments
- **Recordkeeping** - Timestamped timelines and tracked predictions

---

## Using the Core (start here)

**`CORE.md`** is the self-contained activation file. It packs the entire Zbigniew Protocol methodology into a single document you can drop into any AI session.

### How to use it:

1. **With Claude Code / Claude Projects**: Copy `CORE.md` into your project instructions or paste at session start
2. **With ChatGPT**: Paste `CORE.md` into Custom Instructions or at the start of a conversation
3. **With any LLM**: Paste the activation prompt from `CORE.md` (120-token or 300-token version) before your research query
4. **Standalone reading**: `CORE.md` documents the full methodology - confidence levels, cui bono, pattern mapping, source verification, validation gate, etc.

### Domain-specific guides (`_guides/`):

Use these **together with** `CORE.md` when your research falls into a specific domain:

| Guide | File | Use Case |
|-------|------|----------|
| Supply Chain | `_guides/supply_chain_continuity.md` | Disruption research, continuity management, supplier risk |
| Medical Devices | `_guides/medical_device_materials.md` | Material qualifications, regulatory intelligence, biocompatibility |

Paste `CORE.md` + the relevant guide into your session for domain-tailored intelligence analysis.

### Quick example:

```
# Paste CORE.md, then ask:
"Analyze the semiconductor supply chain risk for European automotive
manufacturers given TSMC's Arizona expansion timeline and EU Chips Act
implementation delays."

# Or with medical devices guide:
"Assess material qualification risks for switching from titanium
to PEEK polymer in Class III spinal implants, considering FDA
predicate history and EU MDR requirements."
```

---

## Core Principles

1. **Verified Sources Only** - Primary documents, quality journalism, no speculation as fact
2. **Cui Bono** - Always ask who benefits. Follow the money, not the narrative
3. **Pattern Recognition** - Individual events are noise; patterns across vectors are signal
4. **Falsifiability** - State what would prove you wrong. Unfalsifiable claims are marketing, not analysis
5. **Timestamp Everything** - Accountability through documentation
6. **Steel-Man the Opposition** - Build the strongest case against your thesis before claiming victory
7. **Check the Architects** - People design institutions. Track records predict behavior

---

## Directory Structure

```
zbigniew-protocol/
├── CLAUDE.md              # Framework entry point (for Claude sessions with full repo)
├── CORE.md                # Self-contained core - DROP THIS INTO ANY AI SESSION
├── README.md              # This file
│
├── _methodology/          # HOW TO THINK (9 documents)
│   ├── cui_bono.md       # Beneficiary analysis + money flow tracing + TCO
│   ├── pattern_mapping.md # Cross-vector recognition + named patterns
│   ├── actor_background_checks.md # Personnel file methodology
│   ├── reasoning_improvements.md  # Steel-man, quantitative ranges, signal watch, source diversity, base rate, versioning
│   ├── source_verification.md
│   ├── confidence_levels.md
│   ├── cognitive_biases.md # 12 biases + Sagan philosophical foundation
│   ├── validation_gate.md  # Source validation iron rules
│   └── persona_stability.md
│
├── _guides/               # DOMAIN-SPECIFIC RESEARCH GUIDES
│   ├── supply_chain_continuity.md    # Supply chain disruption + continuity research
│   └── medical_device_materials.md   # Material qualifications + regulatory intel
│
├── _assessments/          # INTELLIGENCE PRODUCTS
│   ├── active/           # Current assessments
│   ├── archived/         # Historical
│   └── templates/        # Assessment templates
│
├── _timeline/             # EVENT TRACKING
│   ├── events.jsonl      # Timestamped events
│   ├── policies.jsonl    # Policy changes
│   └── statements.jsonl  # Official quotes
│
├── _predictions/          # TRACKED PREDICTIONS
│   ├── active.jsonl      # Open predictions
│   ├── resolved.jsonl    # Confirmed/refuted
│   └── accuracy.md       # Track record
│
├── _validators/           # DATA INTEGRITY TOOLS
│   ├── zbigniew          # CLI: validate, predictions, calibration, overdue, export
│   ├── validate.py       # JSONL schema + cross-reference validation
│   ├── predictions.py    # Prediction tracking + calibration analysis
│   └── schemas/          # JSON Schema for events + predictions
│
├── _sources/              # SOURCE LIBRARY
│   └── index.yaml        # Source index with reliability ratings
│
├── _policy/               # POLICY ENGINE (Poland-specific)
│   ├── POLICY_MAKER.md   # Threat level -> recommendations pipeline
│   ├── poland_strategic_objectives.yaml
│   └── policy_maker.py   # Python recommendation engine
│
├── _simulator/            # STRESS SIMULATOR
│   └── index.html        # Matter.js geopolitical stress model (browser-based)
│
├── _publishing/           # OUTPUT
│   ├── templates/        # Article templates
│   └── style_guide.md    # Writing standards + collapsible evidence format
│
└── _memory/               # DECISION LOG
    ├── assessments.jsonl # Assessment decisions
    └── revisions.jsonl   # Change tracking
```

---

## Assessment Workflow

1. **OBSERVE** - Log events to `_timeline/`
2. **PATTERN** - Map across vectors, identify beneficiaries, check named patterns
3. **ANALYZE** - Apply cui bono, actor background checks, steel-man opposition, base rate comparison
4. **PUBLISH** - Collapsible evidence format (summary layer + expandable details), cite sources, state confidence
5. **TRACK** - Log predictions with signal watches, review monthly, version assessments

## Intellectual Heritage

The Zbigniew Protocol builds on Carl Sagan's *Baloney Detection Kit* (1995) - nine rules for distinguishing science from nonsense. We implement all nine and extend them for geopolitics: adding cui bono analysis, actor background checks, pattern mapping across 7 vectors, prediction accountability with signal watches, and assessment versioning for living documents.

Sagan's kit detects bullshit in science. Zbigniew detects it in geopolitics. Same enemy: confident claims without falsifiable criteria.

---

## Confidence Levels

| Level | Label | Meaning |
|-------|-------|---------|
| 5 | CONFIRMED | Primary source documentation |
| 4 | HIGH | Multiple reliable sources agree |
| 3 | MODERATE | Logical inference from facts |
| 2 | LOW | Single source or circumstantial |
| 1 | SPECULATIVE | Pattern suggests, evidence thin |

---

## License

This framework is released for public use. Attribution appreciated.

---

## Contact

Questions or contributions: [evil1.org](https://evil1.org)

---

*"The question is not 'who is an asset.' The question is: 'Why does this policy portfolio perfectly match the wish-list of adversaries?'"*

**por. Zbigniew**
*Pattern recognition, not prophecy*
