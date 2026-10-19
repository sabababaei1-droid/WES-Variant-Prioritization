
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "results" / "03_cadd_ranked_variants.csv"
OUTPUT_DIR = PROJECT_ROOT / "results"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Input file not found: {INPUT_FILE}\n"
        "Run 04_prioritize_cadd.py first."
    )

df = pd.read_csv(INPUT_FILE, na_values=["NA"])

# Normalize ClinVar labels
df["ClinVar_Significance"] = (
    df["ClinVar_Significance"]
    .fillna("Not provided")
    .astype(str)
    .str.strip()
    .str.lower()
)

# Keep clinically relevant categories separate
classification_map = {
    "pathogenic": "Pathogenic",
    "likely pathogenic": "Likely pathogenic",
    "vus": "VUS",
    "uncertain significance": "VUS",
    "conflicting classifications": "Conflicting classifications",
    "not provided": "Not provided",
    "benign": "Benign",
    "likely benign": "Likely benign",
}

df["ClinVar_Category"] = (
    df["ClinVar_Significance"]
    .map(classification_map)
    .fillna("Other / review needed")
)

# Retain candidates for review; do not label them as confirmed causal variants
candidate_categories = {
    "Pathogenic",
    "Likely pathogenic",
    "VUS",
    "Conflicting classifications",
    "Not provided",
    "Other / review needed",
}

candidates_df = df[
    df["ClinVar_Category"].isin(candidate_categories)
].copy()

# Sort for review: classification first, then CADD score
category_order = {
    "Pathogenic": 0,
    "Likely pathogenic": 1,
    "VUS": 2,
    "Conflicting classifications": 3,
    "Not provided": 4,
    "Other / review needed": 5,
}

candidates_df["Review_Order"] = (
    candidates_df["ClinVar_Category"].map(category_order)
)

candidates_df = candidates_df.sort_values(
    by=["Review_Order", "CADD"],
    ascending=[True, False],
    na_position="last",
)

OUTPUT_FILE = OUTPUT_DIR / "04_candidate_variants.csv"
candidates_df.to_csv(OUTPUT_FILE, index=False)

print(f"Variants available for review: {len(candidates_df)}")
print("\nClinVar category counts:")
print(candidates_df["ClinVar_Category"].value_counts())
print(f"\nSaved to: {OUTPUT_FILE}")
