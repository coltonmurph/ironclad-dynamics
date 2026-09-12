## Executive Question: Where is spending growing in the unmanned systems market?

## Analysis Method:
Pulled contracts from USA Spending NAICS 336411 + 334511, DOD, FY 22-25, filtered to find drone specific contracts using keywords against the contract descriptions. 171 out of the 10729 were most defintely about drone contracts. I then group by fiscal year in Postgres/pandas.

## The headline finding - 
CAGR number came out to across the period to -20.5% but could be misleading since we only have 4 data points. Contract count went from 50 -> 40 -> 30 -> 51 across FY 22-25, while average contract value dropped from 55 million to 13 million about a 76% drop. Total dollar volume looks like a decline but that is driven by large contracts in FY2023, not a real shrinking market.

## Why it matters for Ironclad Dynamics -
a market trending towards smaller contracts is possibly more accesible to a midsize firm rather than one dominated by a few massive prime only awards. Needs to be tested against vendor concentration data.  A single large contract is much riskier than a diversified portfolio  of multiple contracts, losing one would be less hurt making it better for Ironclad to enter but nees to be tested against vendor data. Early stage programs tend to have smaller contracts with many programs competing 

## Limitations:
Annual growth over only 4 data points is volatile, keyword based filters may miss contracts using terminology that I did not use or catch platform names in unrealated context. Total_obligated_amount is the full lifetime cumulative value of a contract, atrributed to the contract from FY's when the contract started regardless of when money was obligated. A contract that began in FY23 and runs to FY25 would have all obligated money in the FY23 bucket.
