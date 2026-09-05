import pandas as pd

df = pd.read_csv("results/rare_variants.csv")

high_cadd = df[df["CADD"] >= 20]

high_cadd.to_csv("results/high_cadd_variants.csv", index=False)

print(high_cadd)
