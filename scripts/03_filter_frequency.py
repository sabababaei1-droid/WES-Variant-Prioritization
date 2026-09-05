import pandas as pd

df = pd.read_csv("data/variants.csv")

rare = df[df["gnomAD_AF"] <= 0.01]

print(rare)
