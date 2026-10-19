
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "results" / "04_candidate_variants.csv"
OUTPUT_DIR = PROJECT_ROOT / "results"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Input file not found: {INPUT_FILE}\n"
        "Run 05_select_candidates.py first."
    )

df = pd.read_csv(INPUT_FILE, na_values=["NA"])

df["Zygosity"] = (
    df["Zygosity"].fillna("Unknown").astype(str).str.strip().str.lower()
)
df["Inheritance"] = (
    df["Inheritance"].fillna("Unknown").astype(str).str.strip().str.upper()
)

def review_inheritance(row):
    zygosity = row["Zygosity"]
    inheritance = row["Inheritance"]

    if inheritance == "AR" and zygosity == "hom":
        return "Compatible: homozygous with AR"

    if inheritance == "AR" and zygosity == "het":
        return "Review: check for a second allele"

    if inheritance == "AD" and zygosity in {"het", "hom"}:
        return "Potentially compatible with AD"

    if inheritance in {"UNKNOWN", "NA", ""}:
        return "Review: inheritance unknown"

    return "Review: check genotype and inheritance"

df["Inheritance_Review"] = df.apply(review_inheritance, axis=1)

OUTPUT_FILE = OUTPUT_DIR / "05_inheritance_review.csv"
df.to_csv(OUTPUT_FILE, index=False)

print(f"Variants reviewed: {len(df)}")
print("\nInheritance review summary:")
print(df["Inheritance_Review"].value_counts())
print(f"\nSaved to: {OUTPUT_FILE}")
