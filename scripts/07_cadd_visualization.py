
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_excel("patient4_candidates.xlsx")


plt.figure(figsize=(10, 6))

plt.bar(
    df["GENE"],
    df["CADD_score"], color="skyblue"
)


plt.xlabel("Gene")

plt.ylabel("CADD Score")

plt.title("CADD Score of Prioritized Variants")

plt.axhline(
    20,
    linestyle="--",
    label="CADD threshold = 20"
)

for i, value in enumerate(df["CADD_score"]):

    plt.text(
        i,
        value,
        str(value),
        ha="center",
        va="bottom"
    )

plt.legend()

plt.xticks(rotation=45)

plt.savefig(
    "figures/CADD_score_prioritized_variants.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()