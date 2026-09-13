# Ironclad Dynamics — Federal Market Expansion Analysis

A business analytics case study using real federal procurement data to answer a
strategic question: should a mid-size defense subcontractor expand into the
unmanned systems market, and if so, where?

*Ironclad Dynamics is a fictional client built for this project. The data,
analysis, and findings are real.*

## The Question

Ironclad Dynamics is a mid-size defense company doing sensor and avionics work
on legacy aircraft programs. Leadership wants to know whether unmanned systems
is worth entering — and if it is, which agencies, vendors, and regions actually
offer a way in.

The analysis is built around four executive questions:

1. **Where is spending growing?**
2. **How difficult is the market to enter?**
3. **Who should we sell to?**
4. **Where should we focus geographically?**

## Key Findings

**The market is fragmenting, not shrinking.** Total dollars declined across
FY22–FY25, but contract volume held steady (50 → 40 → 30 → 51) while average
contract size dropped 76% ($55M → $13M). More opportunities, smaller each — a
better shape for a mid-size entrant than the market's headline decline suggests.

**One company owns half the market.** General Atomics holds 53.8% of all
unmanned systems spend. Market HHI is 3,296 (highly concentrated); excluding
General Atomics it drops to 1,878 (moderately concentrated). The barrier isn't
the market — it's one incumbent.

**Concentration is branch-specific, and the Navy is the outlier.**

| Branch | Spend | HHI | Dominant Vendor |
|---|---|---|---|
| Air Force | $3.74B | 6,191 | General Atomics (76.9%) |
| Army | $1.07B | 5,385 | AeroVironment (70.4%) |
| SOCOM | $357M | 9,144 | Single-vendor |
| Navy | $190M | 1,939 | None — 13 active vendors |

An initial hypothesis that the Army was open (General Atomics is absent there)
was tested and disproved — the Army just has a different incumbent.

**Geography mirrors the same story.** California holds $4.61B and 88 of 171
contracts, but four incumbents account for ~98% of it. Navy work centers on
Maryland instead ($98.1M), driven by two mid-size firms near DoD test
infrastructure — a scale Ironclad can credibly match.

**Recommendation:** Navy-first entry through the Maryland defense corridor,
with Air Force and Army pursued later via subcontracting rather than direct
competition. Full reasoning in `docs/recommendation-memo.md`.

## Data & Method

**Source:** USASpending.gov Custom Award Data — DoD prime contract awards,
NAICS 336411 (Aircraft Manufacturing, includes UAVs) and 334511 (Search,
Detection, Navigation & Guidance Systems), FY2022–FY2025, awards $250K+.

**Pipeline:**
1. Raw CSV (~10,700 contracts, 280 columns) trimmed to 21 analysis columns in pandas
2. Loaded into PostgreSQL via SQLAlchemy
3. Unmanned systems contracts isolated (171) through keyword screening of
   contract descriptions — including platform designations (MQ-9, Reaper,
   ScanEagle, Switchblade) alongside generic terms, which roughly doubled recall
4. Vendor names normalized to merge punctuation and whitespace variants
5. Aggregation and metrics (CAGR, HHI, concentration ratios) computed in pandas
6. Results visualized in Tableau

**Herfindahl-Hirschman Index (HHI)** is used to measure vendor concentration:
each vendor's market share is squared and summed, scaled to 10,000. DOJ
thresholds: under 1,500 unconcentrated, 1,500–2,500 moderate, above 2,500
highly concentrated.

## Stack

- **PostgreSQL** — contract data storage and querying
- **Python / pandas** — cleaning, keyword filtering, derived metrics
- **Tableau** — two-page executive dashboard

## Repo Structure

```
data/
  raw/        raw USASpending.gov download (gitignored — too large)
  curated/    filtered analysis dataset
sql/          schema definition
src/          Postgres load script
notebooks/    analysis, one notebook per executive question
tableau/      executive dashboard (.twbx)
docs/         findings docs and recommendation memo
```

## Findings Docs

Each executive question has its own write-up in `docs/`, covering the question,
method, findings, business implications, and limitations:

- `growth-analysis-findings.md`
- `vendor-concentration-analysis.md`
- `branch-analysis.md`
- `geographic-analysis.md`
- `recommendation-memo.md` — the synthesis

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Requires a local PostgreSQL database named `ironclad_dynamics`, and a `.env`
file containing `DB_PASSWORD=yourpassword`.

Load the data:
```bash
python src/load_to_postgres.py
```

## Known Limitations

- `total_obligated_amount` reflects total lifetime contract value attributed to
  the award's start year, not year-of-disbursement spend. Multi-year contracts
  therefore concentrate their full value in one fiscal year, inflating
  year-over-year volatility. Prorating across period of performance would be the
  next refinement.
- Keyword-based identification of unmanned systems contracts may miss awards
  using terminology outside the keyword set.
- Navy findings rest on 20 contracts; HHI at that sample size is sensitive to
  individual awards.
- Seven contracts (4%) lack a US place-of-performance value, likely foreign
  military sales.
- Prime awards only — subcontract activity is not captured in this dataset.
