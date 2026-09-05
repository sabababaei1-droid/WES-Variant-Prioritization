import pandas as pd

initial = len(pd.read_csv("data/variants.csv"))

functional = pd.read_csv("results/functional_variants.csv")
rare = pd.read_csv("results/rare_variants.csv")
high_cadd = pd.read_csv("results/high_cadd_variants.csv")
candidates = pd.read_csv("results/candidate_variants.csv")

functional_percent = (len(functional) / initial) * 100
rare_percent = (len(rare) / initial) * 100
high_cadd_percent = (len(high_cadd) / initial) * 100
candidate_percent = (len(candidates) / initial) * 100

print("Variant Prioritization Summary")
print("------------------------------")

print("Initial variants:", initial)
print("Functional variants:", len(functional), f"({functional_percent:.0f}%)")
print("Rare variants:", len(rare), f"({rare_percent:.0f}%)")
print("High-CADD variants:", len(high_cadd), f"({high_cadd_percent:.0f}%)")
print("Candidate variants:", len(candidates), f"({candidate_percent:.0f}%)")