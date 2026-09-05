import pandas as pd

df = pd.read_csv("results/functional_variants.csv")

rare = df[df["gnomAD_AF"] <= 0.01]

rare.to_csv("results/rare_variants.csv", index=False)

print(rare)
