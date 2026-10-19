
from pathlib import Path

import pandas as pd

# Locate the project root and input file
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "variants.csv"

# Load the educational variant dataset
df = pd.read_csv(INPUT_FILE, na_values=["NA"])

# Validate the required columns
required_columns = [
    "Gene",
    "Variant",
    "Consequence",
    "gnomAD_AF",
    "CADD",
    "ClinVar_Significance",
    "Zygosity",
    "Inheritance",
    "SIFT",
    "PolyPhen2",
]

missing_columns = set(required_columns) - set(df.columns)

if missing_columns:
    raise ValueError(
        f"Missing required columns: {sorted(missing_columns)}"
    )

# Convert annotation columns to numeric values
numeric_columns = ["gnomAD_AF", "CADD", "SIFT", "PolyPhen2"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Display a dataset overview
print("Dataset loaded successfully.")
print(f"Number of variants: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print("\nColumn data types:")
print(df.dtypes)
print("\nFirst five variants:")
print(df.head())
print("\nMissing values per column:")
print(df.isna().sum())
