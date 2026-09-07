import pandas as pd

initial = len(pd.read_csv("data/variants.csv"))

functional = pd.read_csv("results/01_functional_variants.csv")
rare = pd.read_csv("results/02_rare_variants.csv")
high_cadd = pd.read_csv("results/03_high_cadd_variants.csv")
candidates = pd.read_csv("results/04_candidate_variants.csv")

functional_percent = (len(functional) / initial) * 100
rare_percent = (len(rare) / initial) * 100
high_cadd_percent = (len(high_cadd) / initial) * 100
candidate_percent = (len(candidates) / initial) * 100

print("Variant Prioritization Summary")
print("------------------------------")

print("Initial variants:", initial)
print("Functional variants:", len(functional), "(", functional_percent, "%)")
print("Rare variants:", len(rare), "(", rare_percent, "%)")
print("High-CADD variants:", len(high_cadd), "(", high_cadd_percent, "%)")
print("Candidate variants:", len(candidates), "(", candidate_percent, "%)")
