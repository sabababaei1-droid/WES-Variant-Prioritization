
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "results" / "01_functional_variants.csv"
OUTPUT_DIR = PROJECT_ROOT / "results"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Input file not found: {INPUT_FILE}\n"
        "Run 02_filter_functional.py first."
    )

df = pd.read_csv(INPUT_FILE, na_values=["NA"])

# Convert allele frequency to numeric values
df["gnomAD_AF"] = pd.to_numeric(df["gnomAD_AF"], errors="coerce")

# Keep variants with known allele frequency at or below 1%
MAX_AF = 0.01

known_af = df["gnomAD_AF"].notna()
rare_mask = known_af & (df["gnomAD_AF"] <= MAX_AF)

rare_df = df.loc[rare_mask].copy()
unknown_af_df = df.loc[~known_af].copy()

OUTPUT_FILE = OUTPUT_DIR / "02_rare_variants.csv"
UNKNOWN_OUTPUT_FILE = OUTPUT_DIR / "02_unknown_frequency.csv"

rare_df.to_csv(OUTPUT_FILE, index=False)
unknown_af_df.to_csv(UNKNOWN_OUTPUT_FILE, index=False)

print(f"Input variants: {len(df)}")
print(f"Variants with AF <= {MAX_AF}: {len(rare_df)}")
print(f"Variants with unknown AF: {len(unknown_af_df)}")
print(f"Variants excluded for AF > {MAX_AF}: "
      f"{len(df) - len(rare_df) - len(unknown_af_df)}")
print(f"Rare variants saved to: {OUTPUT_FILE}")
print(f"Unknown-frequency variants saved to: {UNKNOWN_OUTPUT_FILE}")
