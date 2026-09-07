import pandas as pd

df = pd.read_csv("results/high_cadd_variants.csv")

candidates = df[
    df["ClinVar_Significance"] == "Pathogenic"
]

candidates.to_csv("results/candidate_variants.csv", index=False)

print(candidates)
