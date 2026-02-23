# ZBIGNIEW POLICY MAKER

**Strategic Policy Generation for Poland**

*Pattern-based policy recommendations from geopolitical assessment*

---

## Overview

The Policy Maker module generates actionable policy recommendations for Poland based on:

1. **Current geopolitical assessment** (from ZBIGNIEW Protocol assessments)
2. **Strategic objectives** (defined in `objectives/poland_strategic_objectives.yaml`)
3. **Active predictions** (from `_predictions/active.jsonl`)
4. **Timeline events** (from `_timeline/events.jsonl`)

Output: Recommendations for 1-year, 5-year, and 20-year horizons with cui bono analysis.

---

## Quick Start

```bash
# Generate full policy report
python3 _policy/engine/policy_maker.py

# Check current threat level
python3 _policy/engine/policy_maker.py threat

# Export as JSON
python3 _policy/engine/policy_maker.py export
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    ZBIGNIEW POLICY MAKER                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐         │
│  │ Assessments  │   │ Predictions  │   │   Events     │         │
│  │ (ZBIGNIEW)   │   │ (active)     │   │  (timeline)  │         │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘         │
│         │                  │                  │                 │
│         └────────────┬─────┴──────────────────┘                 │
│                      │                                          │
│              ┌───────▼───────┐                                  │
│              │ Threat Level  │                                  │
│              │  Assessment   │                                  │
│              └───────┬───────┘                                  │
│                      │                                          │
│         ┌────────────┼────────────┐                             │
│         ▼            ▼            ▼                             │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐                   │
│  │ 1-Year Rec │ │ 5-Year Rec │ │20-Year Rec │                   │
│  └────────────┘ └────────────┘ └────────────┘                   │
│                      │                                          │
│              ┌───────▼───────┐                                  │
│              │  Cui Bono     │                                  │
│              │  Analysis     │                                  │
│              └───────┬───────┘                                  │
│                      │                                          │
│              ┌───────▼───────┐                                  │
│              │ Policy Report │                                  │
│              └───────────────┘                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Strategic Objectives (Summary)

### Tier 1: Existential (Non-negotiable)
- **OBJ_SEC_001**: Territorial Integrity & Security
- **OBJ_SOV_001**: Decision-Making Sovereignty

### Tier 2: Structural (10-20 year foundation)
- **OBJ_ECON_001**: Economic Resilience
- **OBJ_LEAD_001**: Central European Leadership
- **OBJ_INST_001**: Efficient Institutions

### Tier 3: Quality of Life (5-10 year improvements)
- **OBJ_HEALTH_001**: Healthcare System Reform
- **OBJ_TAX_001**: Tax System Optimization
- **OBJ_LIVING_001**: Living Standards Maintenance

### Tier 4: Strategic Positioning (5-20 year vision)
- **OBJ_EU_001**: EU Relationship Optimization
- **OBJ_VALUES_001**: Traditional Values with Liberty
- **OBJ_SAFE_001**: Safe Society

---

## Recommendation Structure

Each recommendation includes:

| Field | Description |
|-------|-------------|
| `id` | Unique identifier (REC_YYYY_NNN) |
| `title` | Brief title |
| `description` | Full description |
| `horizon` | 1_year / 5_year / 20_year |
| `priority` | CRITICAL / HIGH / MEDIUM / LOW |
| `vectors` | INSTITUTIONAL, ALLIANCE, ECONOMIC, etc. |
| `objectives_served` | Which strategic objectives this serves |
| `actions` | Specific action items |
| `resources_required` | Fiscal/political resources needed |
| `risks` | What could go wrong |
| `cui_bono` | Who benefits, who opposes |
| `confidence` | 0-1 confidence level |
| `metrics` | How to measure success |

---

## Cui Bono Analysis

Every recommendation includes:

```yaml
cui_bono:
  primary_beneficiaries: [...]   # Main winners
  secondary_beneficiaries: [...]  # Also benefits
  potential_losers: [...]         # Harmed by policy
  who_opposes: "..."              # Expected opposition
```

This follows the ZBIGNIEW Protocol principle: **"Follow the incentives, not the rhetoric."**

---

## Threat Level Assessment

Based on active predictions and events:

| Level | Meaning | Trigger |
|-------|---------|---------|
| **ELEVATED** | Immediate threats | Military predictions active OR 3+ imminent predictions |
| **HEIGHTENED** | Significant stress | 2+ alliance-related predictions active |
| **BASELINE** | Normal operations | No imminent threats |

---

## Red Lines (Non-Negotiable)

From strategic objectives:

- No mandatory migrant quotas
- No EU taxation without unanimity
- No judicial supremacy without treaty change
- No defense integration that undermines NATO

---

## Integration with nSENS

The Policy Maker can be enhanced with nSENS personas:

| Persona | Application |
|---------|-------------|
| **ZBIGNIEW** | Geopolitical assessment, shadow sensing |
| **MIDAS** | ROI analysis of policy costs/benefits |
| **NASH** | Game theory for stakeholder analysis |
| **SENECA** | Risk assessment, antifragility |
| **DARO** | Reality check on implementation |

### Future Integration

```python
# Planned: Multi-persona policy validation
def validate_with_personas(recommendation):
    perspectives = []
    perspectives.append(zbigniew_assessment(rec))  # Strategic implications
    perspectives.append(midas_roi(rec))            # Cost/benefit
    perspectives.append(nash_game_theory(rec))     # Stakeholder dynamics
    perspectives.append(seneca_risk(rec))          # Downside scenarios
    perspectives.append(daro_reality(rec))         # Implementation feasibility
    return synthesize(perspectives)
```

---

## Integration with Stress Simulator

The Policy Maker recommendations can be tested in the physics simulator:

1. Load recommendation scenario
2. Apply forces based on policy actions
3. Observe stress propagation
4. Detect cascade risks
5. Refine recommendations

---

## Output Formats

### Console Report
```bash
python3 _policy/engine/policy_maker.py
```

### JSON Export
```bash
python3 _policy/engine/policy_maker.py export
# Output: _policy/recommendations/assessment_YYYY-MM-DD.json
```

---

## Updating Objectives

Edit `_policy/objectives/poland_strategic_objectives.yaml`:

```yaml
objectives:
  tier_1_existential:
    - id: OBJ_NEW_001
      name: "New Objective"
      description: "..."
      priority: 1
      metrics:
        - "Measurable outcome 1"
        - "Measurable outcome 2"
```

---

## Monitoring & Revision

### Quarterly Review
- Economic indicators
- Security situation
- EU relations

### Annual Review
- Full objectives progress
- Constraint compliance
- External threat assessment

### Trigger-Based Review
- Major geopolitical event
- Government change
- Economic crisis
- Alliance stress

---

## Philosophy

> "Poland's security comes not from isolation, but from being indispensable.
> Our sovereignty is protected not by walls, but by choices we retain.
> Our values are preserved not by mandates, but by example."

---

## See Also

- [Strategic Objectives](objectives/poland_strategic_objectives.yaml)
- [ZBIGNIEW Protocol](../CLAUDE.md)
- [Prediction Tracker](../_validators/predictions.py)
- [Stress Simulator](../_simulator/index.html)
