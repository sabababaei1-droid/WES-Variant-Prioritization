import pandas as pd

df = pd.read_csv("data/variants.csv")

functional = df[df["Consequence"].isin([
    "missense",
    "frameshift",
    "stop_gained"
])]

print(functional)
