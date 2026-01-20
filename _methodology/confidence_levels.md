# CONFIDENCE LEVELS FRAMEWORK

*Every assessment carries uncertainty. Make it explicit.*

---

## THE FIVE LEVELS

| Level | Label | Probability | Meaning |
|-------|-------|-------------|---------|
| **5** | CONFIRMED | >95% | Direct primary source evidence |
| **4** | HIGH | 75-95% | Multiple reliable sources agree |
| **3** | MODERATE | 50-75% | Logical inference from confirmed facts |
| **2** | LOW | 25-50% | Single source or circumstantial |
| **1** | SPECULATIVE | <25% | Pattern suggests but evidence thin |

---

## LEVEL DEFINITIONS

### Level 5: CONFIRMED
**Standard**: Primary source documentation exists

**Examples**:
- Official government document states X
- Video/audio recording confirms statement
- Court filing establishes fact
- Multiple independent primary sources agree

**Language**: "X is confirmed by [source]"

### Level 4: HIGH CONFIDENCE
**Standard**: Multiple reliable sources agree without contradiction

**Examples**:
- Three quality journalists independently report same claim
- Academic consensus with documented methodology
- Official source + institutional analysis alignment

**Language**: "Evidence strongly suggests X" / "X is highly likely"

### Level 3: MODERATE CONFIDENCE
**Standard**: Logical inference from confirmed facts, or mixed sourcing

**Examples**:
- Pattern of confirmed facts points to conclusion
- Reliable source claims something unverifiable
- Circumstantial evidence is strong but not conclusive

**Language**: "Available evidence indicates X" / "X is probable"

### Level 2: LOW CONFIDENCE
**Standard**: Single source, circumstantial, or contested

**Examples**:
- One source claims something others don't
- Inference requires assumptions
- Competing explanations equally plausible

**Language**: "Some evidence suggests X" / "X is possible"

### Level 1: SPECULATIVE
**Standard**: Pattern-based hypothesis with thin evidence

**Examples**:
- "If this pattern continues..."
- Inference from behavior, not evidence
- Scenario analysis

**Language**: "If X is true, then..." / "One possibility is X"

---

## CONFIDENCE RULES

### Rule 1: Label Everything
Every factual claim needs a confidence level, explicitly or implicitly.

### Rule 2: Highest Common Denominator
A chain of reasoning is only as strong as its weakest link.
- HIGH + HIGH = HIGH
- HIGH + MODERATE = MODERATE
- HIGH + LOW = LOW

### Rule 3: Never Present Low as High
- Level 1-2 claims must be labeled as uncertain
- "According to [source]" not "[Source] confirms"
- "May indicate" not "proves"

### Rule 4: Update When Evidence Changes
- New confirming evidence: consider upgrading
- New contradicting evidence: consider downgrading
- Document the change in `_memory/revisions.jsonl`

---

## CONFIDENCE DOCUMENTATION

In assessments, document confidence like this:

```markdown
## Key Judgments

1. **Russia benefits from NATO fracture** (CONFIRMED - Level 5)
   - Primary source: Russia NSS 2021, FPC 2023
   - Russia's own documents state this as objective

2. **Current policies weaken NATO cohesion** (HIGH - Level 4)
   - Multiple vectors: tariffs on allies, territorial threats, reduced commitment
   - Sources: [list sources]

3. **Policy designers intended this outcome** (MODERATE - Level 3)
   - Inference from: pattern consistency, Project 2025 documentation
   - Alternative explanation: ideological convergence without intent

4. **Foreign coordination exists** (LOW - Level 2)
   - Would require classified intelligence to confirm
   - Observable pattern is consistent with but doesn't prove coordination
```

---

## LANGUAGE GUIDE

### Level 5 Language
- "is" / "confirms" / "establishes" / "documents"
- "According to [primary source]"
- "The document states"

### Level 4 Language
- "strongly suggests" / "indicates clearly" / "high confidence"
- "Multiple sources report" / "Evidence points to"
- "Is highly likely" / "Almost certainly"

### Level 3 Language
- "suggests" / "indicates" / "probable" / "likely"
- "Evidence is consistent with"
- "Reasonable to conclude"

### Level 2 Language
- "may" / "might" / "possible" / "some evidence suggests"
- "Could indicate" / "One interpretation"
- "If accurate, would suggest"

### Level 1 Language
- "if true" / "hypothetically" / "scenario"
- "Pattern might suggest" / "Could potentially"
- "Speculation" / "Unverified"

---

## AGGREGATING CONFIDENCE

When combining multiple assessments:

### Supporting Evidence (Same Direction)
- 3 x Level 3 = Level 4 (convergent moderate evidence)
- 2 x Level 4 = Level 4+ (reinforcing)
- Level 5 + Level 4 = Level 5 (primary source wins)

### Contradicting Evidence
- Level 4 vs Level 4 = Level 3 (contested)
- Level 5 vs Level 4 = Level 5 prevails
- Level 3 vs Level 3 = Level 2 (unresolved)

### Mixed Evidence
- Note the conflict explicitly
- Present both sides
- Let reader assess

---

## COMMON ERRORS

1. **Confidence Inflation**
   - Wanting something to be true increases perceived confidence
   - Check: Would I rate this the same if it contradicted my view?

2. **Source Conflation**
   - Multiple sources citing same original = 1 source, not multiple
   - Check: Are these truly independent?

3. **Inference Stacking**
   - Each inference step reduces confidence
   - A → B (Level 4) → C (Level 3) → D (Level 2)

4. **Asymmetric Skepticism**
   - Being skeptical of disconfirming evidence, credulous of confirming
   - Check: Am I applying the same standard to both?

---

## REMEMBER

> "It ain't what you don't know that gets you into trouble.
> It's what you know for sure that just ain't so." - Mark Twain

Overconfidence kills analysis.
Explicit uncertainty is intellectual honesty.
