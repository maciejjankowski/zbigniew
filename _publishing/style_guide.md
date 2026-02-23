# ZBIGNIEW PROTOCOL STYLE GUIDE

*How we write. Why it matters.*

---

## VOICE

### Tone
- **Authoritative but humble**: Confident in methodology, honest about uncertainty
- **Direct**: No hedging when evidence is clear
- **Accessible**: Expert analysis, civilian language
- **Pattern-focused**: Let data speak, minimize editorializing

### Perspective
- First person sparingly ("I assess", "My analysis")
- Institutional voice for methodology ("The protocol requires")
- Never preach or moralize

---

## STRUCTURE

### Every Piece Includes:
1. **Date** - Always timestamped
2. **Confidence level** - Explicit uncertainty
3. **Sources** - Linked and cited
4. **Beneficiary analysis** - Who gains?
5. **Falsifiability** - What would disprove this?

### Information Hierarchy:
1. **BLUF** (Bottom Line Up Front) - Lead with conclusion
2. **Key judgments** - Numbered, confidence-rated
3. **Evidence** - Supporting analysis
4. **Alternatives** - Other explanations
5. **Sources** - Full citations

---

## LANGUAGE

### DO:
- Use precise language
- Define terms on first use
- Cite sources inline
- State confidence explicitly
- Acknowledge uncertainty
- Use tables for comparisons
- Use collapsible sections for details

### DON'T:
- Use weasel words ("some say", "many believe")
- Make claims without sources
- Present speculation as fact
- Use emotional language
- Editorialize excessively
- Assume reader knowledge

---

## CONFIDENCE LANGUAGE

| Level | Use These Words | Avoid These |
|-------|-----------------|-------------|
| 5 | confirms, establishes, documents | - |
| 4 | strongly suggests, highly likely | proves, definitely |
| 3 | indicates, suggests, probable | clearly, obviously |
| 2 | may, possible, some evidence | likely, probably |
| 1 | if true, hypothetically, speculative | suggests, indicates |

---

## COLLAPSIBLE EVIDENCE FORMAT

The Zbigniew Protocol uses a **layered reading** approach across all output formats. Every piece has a summary layer (readable in minutes) and expandable evidence (for skeptics and analysts).

### The Pattern: Summary → Expandable Evidence

```markdown
**1. Key Judgment Title** (Confidence: HIGH)

Visible summary — 1-2 sentences that stand alone. The reader gets the conclusion without clicking.

<details markdown="1">
<summary markdown="0"><strong>▶ Evidence & Sources</strong></summary>

Full sourced analysis here. Tables, lists, links, quotes — all render correctly.

| Data | Source | Confidence |
|------|--------|------------|
| ...  | ...    | ...        |

**Strongest Case Against This Judgment:**
[Steel-man the opposition]

Sources: [Name](URL), [Name](URL)

</details>
```

### Where to Use Collapsible Sections

| Format | What's Visible | What's Collapsible |
|--------|---------------|-------------------|
| **Full Assessment** | Executive summary, key judgment summaries, predictions, bottom line | Evidence per judgment, background, cui bono, pattern mapping, personnel files, alternatives, red team, sources |
| **Article / Blog Post** | Narrative flow, key claims, conclusion | Supporting data, source lists, methodology notes |
| **LinkedIn Post** | No collapsibles — LinkedIn doesn't support HTML. Keep it flat, link to full assessment |
| **Intelligence Brief** | All visible — briefs are already short |

### Reading Time Targets

| Layer | Target | Label |
|-------|--------|-------|
| Summary (no clicks) | 5-10 min | "X min summary" |
| Full (all expanded) | 25-40 min | "Y min full analysis" |
| State both in frontmatter | — | `reading_time: "8 min summary / 35 min full analysis"` |

### Jekyll / kramdown Rules

When publishing to Jekyll sites:
- `<details markdown="1">` — enables markdown rendering inside
- `<summary markdown="0">` — prevents kramdown from breaking the summary tag
- Blank line after `</summary>` and before `</details>` — required
- Blank line before tables inside `<details>` — required

---

## SOURCING FORMAT

### Inline Citation:
> According to [Russia's 2021 National Security Strategy](link), the United States is designated as an "unfriendly state."

### Collapsible Excerpt:
```markdown
<details markdown="1">
<summary markdown="0"><strong>Key Excerpt</strong></summary>

> "Exact quote from source"
>
> — Source Name, Date

</details>
```

### Source List:
```markdown
**Sources**:
- [Source Title](URL) | [Reliability: HIGH]
- [Source Title](URL) | [Reliability: MODERATE]
```

---

## TABLES

Use tables for:
- Beneficiary analysis
- Pattern mapping
- Timeline comparisons
- Confidence summaries

Format:
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data | Data | Data |
```

---

## HEADINGS

- **H1**: Title only (one per document)
- **H2**: Major sections
- **H3**: Subsections
- **H4**: Minor points (use sparingly)

Use ALL CAPS for section labels sparingly (EXECUTIVE SUMMARY, KEY JUDGMENTS)

---

## FORMATTING

### Emphasis:
- **Bold** for key terms, names, critical points
- *Italic* for quotes, foreign terms, titles
- `Code` for technical terms, IDs

### Lists:
- Numbered for sequences, rankings, procedures
- Bullets for unordered items
- Nested lists for hierarchy

### Horizontal Rules:
Use `---` to separate major sections

---

## LENGTH GUIDELINES

| Format | Target Length | Max Length |
|--------|---------------|------------|
| Intelligence Brief | 500 words | 800 words |
| Full Assessment | 2000 words | 4000 words |
| Article | 1500 words | 3000 words |
| Timeline Entry | 100 words | 200 words |

---

## SIGNATURE

Every published piece ends with:

```markdown
**por. Zbigniew**
*Pattern recognition, not prophecy*
*[Date]*

---

*Verify everything. Trust patterns, not prophecies.*
```

---

## COMMON ERRORS

1. **Burying the lede** - Put conclusion first
2. **Vague attribution** - Name sources specifically
3. **Confidence inflation** - When uncertain, say so
4. **Missing falsifiability** - Always state what would disprove
5. **Excessive hedging** - Be direct when evidence is clear
6. **No beneficiary analysis** - Always ask who gains

---

## REVIEW CHECKLIST

Before publishing:

- [ ] Timestamped with date
- [ ] Confidence level stated
- [ ] All claims sourced
- [ ] Cui bono analysis included
- [ ] Falsifiability stated
- [ ] Bias check completed
- [ ] Alternatives considered
- [ ] Collapsible evidence format applied (summary visible, evidence expandable)
- [ ] Reading time stated (summary / full)
- [ ] `markdown="1"` on `<details>`, `markdown="0"` on `<summary>` (if Jekyll)
- [ ] Style guide followed
- [ ] Proofread for clarity
