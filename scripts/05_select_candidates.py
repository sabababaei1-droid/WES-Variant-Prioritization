import pandas as pd

df = pd.read_csv("results/high_cadd_variants.csv")

candidates = df[
    (df["Consequence"].isin([
        "missense",
        "frameshift",
        "stop_gained"
    ]))
]

candidates.to_csv("results/candidate_variants.csv", index=False)

print(candidates)
