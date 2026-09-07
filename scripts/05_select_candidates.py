import pandas as pd

df = pd.read_csv("results/03_high_cadd_variants.csv")

candidates = df[
    df["ClinVar_Significance"] == "Pathogenic"
]

candidates.to_csv("results/04_candidate_variants.csv", index=False)

print(candidates)