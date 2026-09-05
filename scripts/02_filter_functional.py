import pandas as pd

df = pd.read_csv("data/variants.csv")

functional = df[df["Consequence"].isin([
    "missense",
    "frameshift",
    "stop_gained"
])]

functional.to_csv("results/functional_variants.csv", index=False)

print(functional)
