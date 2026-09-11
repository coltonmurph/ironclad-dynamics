**\#Ironclad Dynamics \- Market Expansion Analysis**

&nbsp;

**\*\*Status:\*\*** in progress

&nbsp;

**\#\#Project Overview**:

Ironclad Dynamics is a mid-sized defense company looking to expand its federal contracting business. Using USASpending procurement data, we will determine which markets, agencies and geographic locations offer the strongest opportunities for an expansion.

&nbsp;

**\#\#Business Analysis Questions**:

* Where is spending growing?  
* How difficult is it to enter the market?&nbsp;  
* Who should we sell to?&nbsp;  
* Where should we focus geographically?

&nbsp;

**\#\#Tech Stack**

Postgres- querying raw award data

Python \- Deriving metrics

Tableau \- Building Dashboard

&nbsp;

**\#\#Repo Structure**:

\`\`\`

data/

raw/        raw USASpending.gov award data download (csv)

curated/    cleaned tables, ready for Tableau

sql/          schema definitions \+ analysis queries

notebooks/    exploratory analysis, opportunity score derivation

tableau/      executive dashboard (.twbx)

docs/         client profile, recommendation memo

\`\`\`

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

\#\# Setup

&nbsp;

\`\`\`bash

python \-m venv .venv

source .venv/bin/activate

pip install \-r requirements.txt

\`\`\`

&nbsp;

Requires a local PostgreSQL database named \`ironclad\_dynamics\`.

&nbsp;