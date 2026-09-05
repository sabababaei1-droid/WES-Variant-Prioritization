import pandas as pd

functional = pd.read_csv("results/functional_variants.csv")
rare = pd.read_csv("results/rare_variants.csv")
high_cadd = pd.read_csv("results/high_cadd_variants.csv")
candidates = pd.read_csv("results/candidate_variants.csv")

print("Variant Prioritization Summary")
print("------------------------------")

print("Functional variants:", len(functional))
print("Rare variants:", len(rare))
print("High-CADD variants:", len(high_cadd))
print("Candidate variants:", len(candidates))