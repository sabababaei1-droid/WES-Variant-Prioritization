import pandas as pd

df = pd.read_csv("data/variants.csv")

candidates = df[
    (df["Consequence"].isin([
        "missense",
        "frameshift",
        "stop_gained"
    ]))
    & (df["gnomAD_AF"] <= 0.01)
    & (df["CADD"] >= 20)
]

print(candidates)
