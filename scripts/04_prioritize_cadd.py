import pandas as pd

df = pd.read_csv("data/variants.csv")

high_cadd = df[df["CADD"] >= 20]

print(high_cadd)
