import pandas as pd

df = pd.read_csv("results/functional_variants.csv")

rare = df[df["gnomAD_AF"] <= 0.01]

df = pd.read_csv("results/01_functional_variants.csv")

print(rare)
