
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "variants.csv"
OUTPUT_DIR = PROJECT_ROOT / "results"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE, na_values=["NA"])

# Normalize consequence labels for consistent filtering
df["Consequence"] = df["Consequence"].astype(str).str.strip().str.lower()

# Keep variants with potentially relevant functional consequences
relevant_consequences = {
    "missense",
    "frameshift",
    "stop_gained",
    "splice_donor",
    "splice_acceptor",
    "splice_region",
    "start_lost",
    "stop_lost",
    "inframe_deletion",
    "inframe_insertion",
}

functional_df = df[df["Consequence"].isin(relevant_consequences)].copy()

OUTPUT_FILE = OUTPUT_DIR / "01_functional_variants.csv"
functional_df.to_csv(OUTPUT_FILE, index=False)

print(f"Input variants: {len(df)}")
print(f"Variants retained: {len(functional_df)}")
print(f"Variants excluded: {len(df) - len(functional_df)}")
print(f"Saved to: {OUTPUT_FILE}")
print("\nRetained consequence counts:")
print(functional_df["Consequence"].value_counts())
