
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "results" / "05_inheritance_review.csv"
OUTPUT_DIR = PROJECT_ROOT / "results" / "figures"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Input file not found: {INPUT_FILE}\n"
        "Run 06_inheritance_review.py first."
    )

df = pd.read_csv(INPUT_FILE, na_values=["NA"])
df["CADD"] = pd.to_numeric(df["CADD"], errors="coerce")

plot_df = df.dropna(subset=["CADD"]).copy()

if plot_df.empty:
    print("No valid CADD scores available for plotting.")
else:
    plot_df = plot_df.sort_values("CADD", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(plot_df["Gene"], plot_df["CADD"])
    plt.xlabel("Gene")
    plt.ylabel("CADD score")
    plt.title("CADD Scores Across Educational Variants")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_file = OUTPUT_DIR / "cadd_scores.png"
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Plot saved to: {output_file}")
