import pandas as pd

df = pd.read_csv("results/01_functional_variants.csv")

rare = df[df["gnomAD_AF"] <= 0.01]

rare.to_csv("results/02_rare_variants.csv", index=False)

print(rare)