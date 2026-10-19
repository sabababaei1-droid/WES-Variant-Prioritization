
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"

# Input files
original_file = DATA_DIR / "variants.csv"
functional_file = RESULTS_DIR / "01_functional_variants.csv"
frequency_file = RESULTS_DIR / "02_rare_variants.csv"
candidate_file = RESULTS_DIR / "04_candidate_variants.csv"
cadd_file = RESULTS_DIR / "03_cadd_ranked_variants.csv"
inheritance_file = RESULTS_DIR / "05_inheritance_review.csv"

# Load the original dataset and filtered outputs
original = pd.read_csv(original_file)
functional = pd.read_csv(functional_file)
rare = pd.read_csv(frequency_file)
candidates = pd.read_csv(candidate_file)
cadd = pd.read_csv(cadd_file)
inheritance = pd.read_csv(inheritance_file)

# Use the final candidate list as the master table
final_table = candidates.copy()

# Add CADD prioritization information
if "CADD_Priority" in cadd.columns:
    final_table = final_table.merge(
        cadd[["Gene", "Variant", "CADD_Priority"]],
        on=["Gene", "Variant"],
        how="left"
    )

# Add inheritance review
if "Inheritance_Review" in inheritance.columns:
    final_table = final_table.merge(
        inheritance[["Gene", "Variant", "Inheritance_Review"]],
        on=["Gene", "Variant"],
        how="left"
    )

# Keep a clean, readable column order
preferred_columns = [
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
    "CADD_Priority",
    "Inheritance_Review",
]

columns = [col for col in preferred_columns if col in final_table.columns]
final_table = final_table[columns]

# Save the final table
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
output_file = RESULTS_DIR / "final_candidate_variants.csv"
final_table.to_csv(output_file, index=False)

# Display the complete table in the terminal
print("\nFINAL CANDIDATE VARIANTS")
print("=" * 80)
print(final_table.to_string(index=False))
print(f"\nTotal candidate variants: {len(final_table)}")
print(f"Saved to: {output_file}")
