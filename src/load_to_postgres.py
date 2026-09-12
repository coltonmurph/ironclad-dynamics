"""
Loads the cleaned contracts CSV into the Postgres contracts table.

Run TRUNCATE TABLE contracts; in Postgres before re-running this script,
to avoid inserting duplicate rows.
"""

import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load environment variables (DB_PASSWORD) from .env
load_dotenv()
db_password = quote_plus(os.environ.get("DB_PASSWORD"))

# Build the connection string and engine
connection_string = f"postgresql://postgres:{db_password}@localhost:5432/ironclad_dynamics"
engine = create_engine(connection_string)

# Read the cleaned, curated CSV
df = pd.read_csv("data/curated/contracts_slim.csv")
print(f"Loaded {df.shape[0]} rows from CSV.")

# Load into Postgres
try:
    with engine.begin() as connection:
        df.to_sql("contracts", connection, if_exists="append", index=False)
    print(f"Loaded {df.shape[0]} rows into contracts table.")
except Exception as e:
    print(f"Failed to load data: {e}")