
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "results" / "05_inheritance_review.csv"
OUTPUT_DIR = PROJECT_ROOT / "results"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Input file not found: {INPUT_FILE}\n"
        "Run 06_inheritance_review.py first."
    )

df = pd.read_csv(INPUT_FILE, na_values=["NA"])

print("=" * 50)
print("EDUCATIONAL WES VARIANT PRIORITIZATION SUMMARY")
print("=" * 50)

print(f"\nTotal variants reviewed: {len(df)}")

if "Consequence" in df.columns:
    print("\nVariants by consequence:")
    print(df["Consequence"].value_counts(dropna=False).to_string())

if "ClinVar_Category" in df.columns:
    print("\nVariants by ClinVar category:")
    print(df["ClinVar_Category"].value_counts(dropna=False).to_string())

if "CADD_Priority" in df.columns:
    print("\nVariants by CADD priority:")
    print(df["CADD_Priority"].value_counts(dropna=False).to_string())

if "Inheritance_Review" in df.columns:
    print("\nVariants by inheritance review:")
    print(
        df["Inheritance_Review"]
        .value_counts(dropna=False)
        .to_string()
    )

# Save a compact summary table
summary_rows = []

for column in [
    "Consequence",
    "ClinVar_Category",
    "CADD_Priority",
    "Inheritance_Review",
]:
    if column in df.columns:
        counts = df[column].value_counts(dropna=False)

        for category, count in counts.items():
            summary_rows.append({
                "Annotation": column,
                "Category": str(category),
                "Count": int(count),
            })

summary_df = pd.DataFrame(summary_rows)
OUTPUT_FILE = OUTPUT_DIR / "06_variant_summary.csv"
summary_df.to_csv(OUTPUT_FILE, index=False)

print(f"\nSummary table saved to: {OUTPUT_FILE}")
print("\nReminder: these are synthetic educational data,")
print("not clinical classifications or diagnostic results.")
