
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "results" / "02_rare_variants.csv"
OUTPUT_DIR = PROJECT_ROOT / "results"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Input file not found: {INPUT_FILE}\n"
        "Run 03_filter_frequency.py first."
    )

df = pd.read_csv(INPUT_FILE, na_values=["NA"])

df["CADD"] = pd.to_numeric(df["CADD"], errors="coerce")

# Rank variants by CADD without automatically discarding lower scores
df["CADD_Priority"] = "Unknown"
df.loc[df["CADD"] < 20, "CADD_Priority"] = "Lower"
df.loc[df["CADD"] >= 20, "CADD_Priority"] = "Higher"

ranked_df = df.sort_values(
    by="CADD",
    ascending=False,
    na_position="last"
).copy()

OUTPUT_FILE = OUTPUT_DIR / "03_cadd_ranked_variants.csv"
ranked_df.to_csv(OUTPUT_FILE, index=False)

print(f"Variants ranked: {len(ranked_df)}")
print("\nCADD priority counts:")
print(ranked_df["CADD_Priority"].value_counts())
print(f"\nSaved to: {OUTPUT_FILE}")
print("\nTop variants by CADD:")
print(
    ranked_df[
        ["Gene", "Variant", "CADD", "CADD_Priority"]
    ].head(10).to_string(index=False)
)
