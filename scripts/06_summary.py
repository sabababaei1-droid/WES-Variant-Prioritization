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


print(f"Functional variants: {len(functional)} ({functional_percent:.0f}%)")
print(f"Rare variants: {len(rare)} ({rare_percent:.0f}%)")
print(f"High-CADD variants: {len(high_cadd)} ({high_cadd_percent:.0f}%)")
print(f"Candidate variants: {len(candidates)} ({candidate_percent:.0f}%)")

#or.......

#print("Initial variants:", initial)==Initial variants: 5
#print("Functional variants:", len(functional), "(", functional_percent, "%)")==Functional variants: 4 ( 80.0 %)
#print("Rare variants:", len(rare), "(", rare_percent, "%)")==Rare variants: 3 ( 60.0 %)
#print("High-CADD variants:", len(high_cadd), "(", high_cadd_percent, "%)")==High-CADD variants: 2 ( 40.0 %)
#print("Candidate variants:", len(candidates), "(", candidate_percent, "%)")== Candidate variants: 1 ( 20.0 %)







