# SOURCE VERIFICATION FRAMEWORK

*Verified sources only. No speculation presented as fact.*

---

## SOURCE HIERARCHY

### Tier 1: PRIMARY SOURCES (Highest reliability)
- Official government documents
- Legislation text
- Court filings and decisions
- Official transcripts (verified)
- Treaties and agreements
- Corporate SEC filings
- Academic datasets

**Usage**: Can cite directly as fact
**Verification**: Check official source URL, archive if possible

### Tier 2: INSTITUTIONAL ANALYSIS (High reliability)
- Major think tanks (Brookings, RAND, CSIS, Carnegie, CFR)
- Academic institutions (peer-reviewed)
- Government research services (CRS, GAO, CBO)
- International bodies (UN, NATO official analysis)

**Usage**: Can cite analysis, note institutional perspective
**Verification**: Check author credentials, funding disclosure

### Tier 3: QUALITY JOURNALISM (Moderate-High reliability)
- Major newspapers of record (NYT, WaPo, WSJ, FT, Guardian)
- Wire services (AP, Reuters, AFP)
- Investigative outlets (ProPublica, The Intercept)

**Usage**: Cite specific claims with direct quotes/documents
**Verification**: Check if claim is sourced, look for corroboration
**Caution**: Anonymous sources require corroboration

### Tier 4: SPECIALIZED SOURCES (Moderate reliability)
- Industry publications
- Regional news outlets
- Expert blogs and substacks
- OSINT researchers (Bellingcat, etc.)

**Usage**: Useful for leads, require corroboration
**Verification**: Check track record, methodology transparency

### Tier 5: SOCIAL MEDIA / UNVERIFIED (Low reliability)
- Twitter/X posts
- Telegram channels
- Anonymous sources
- Partisan media

**Usage**: Never cite as fact without independent verification
**Verification**: Treat as leads only, verify through Tier 1-3

---

## VERIFICATION CHECKLIST

Before citing any source:

- [ ] Is this the original source or a secondary report?
- [ ] Can I verify the claim through a second independent source?
- [ ] Is the source's methodology transparent?
- [ ] Does the source have a track record of accuracy?
- [ ] Is there obvious bias that might distort reporting?
- [ ] Have I archived the source in case it disappears?

---

## SOURCE DOCUMENTATION FORMAT

When adding sources to `_sources/index.yaml`:

```yaml
- id: src_2026_001
  title: "Russia's 2021 National Security Strategy"
  type: primary
  tier: 1
  url: "http://publication.pravo.gov.ru/Document/View/0001202107030001"
  archived: "https://web.archive.org/web/..."
  language: russian
  date: 2021-07-02
  reliability: confirmed
  notes: "Official Kremlin publication, primary source for Russian strategic doctrine"

- id: src_2026_002
  title: "Carnegie Analysis of Russia NSS 2021"
  type: analysis
  tier: 2
  url: "https://carnegieendowment.org/posts/2021/07/..."
  author: "Dmitri Trenin"
  institution: "Carnegie Endowment"
  date: 2021-07-05
  reliability: high
  bias_notes: "Carnegie generally centrist, Trenin is Russia expert"
```

---

## RED FLAGS

**Immediate skepticism required:**

1. **Anonymous sources** without corroboration
2. **Single-source** extraordinary claims
3. **Circular sourcing** (A cites B cites A)
4. **Screenshots** without verification
5. **"Sources say"** without specificity
6. **Emotional framing** over factual reporting
7. **Claims that confirm** what you want to believe
8. **Timing** suspiciously convenient to narrative

---

## QUOTATION STANDARDS

### Direct Quotes
- Use exact text in quotation marks
- Include source, date, context
- Link to primary source when possible

### Paraphrase
- Clearly indicate you're summarizing
- Don't put words in mouths
- Link to original for verification

### Disputed Claims
- Note the dispute
- Present multiple perspectives
- Let reader assess

---

## ARCHIVING PROTOCOL

**Why archive**: Sources disappear, pages change, history gets rewritten

**How to archive**:
1. Save to Internet Archive (web.archive.org)
2. Local PDF/screenshot backup
3. Note archive URL in source index

**When to archive**:
- Any primary source you cite
- Any claim that might be contested
- Any source that might be deleted

---

## EXAMPLE SOURCE CHAIN

**Claim**: "Russia's 2021 NSS designates the US as an 'unfriendly state'"

**Source Chain**:
1. **Primary**: Original Russian government document (Tier 1)
2. **Translation**: Official or verified translation
3. **Analysis**: Carnegie Endowment analysis confirming interpretation (Tier 2)
4. **Journalism**: Multiple outlets reporting same (Tier 3)

**Confidence**: HIGH - Primary source + institutional analysis + journalistic corroboration

---

## REMEMBER

> "Extraordinary claims require extraordinary evidence."

The more significant the claim, the higher the verification standard.
When in doubt, don't assert - note the uncertainty.
