# WES Variant Prioritization

A Python-based educational workflow for prioritizing annotated genetic variants from whole-exome sequencing (WES) data.

## Project Overview

This project demonstrates a reproducible variant prioritization workflow using **Python, pandas, and Matplotlib**. It uses a synthetic dataset to illustrate how functional consequences, population allele frequency, ClinVar classifications, CADD scores, zygosity, inheritance patterns, and in-silico prediction scores can be organized for candidate review.

The workflow produces intermediate filtering results, a summary report, a CADD visualization, and a consolidated final table of candidate variants.

## Workflow

1. **Load and validate data** — Check required columns, data types, and missing annotations.
2. **Functional consequence filtering** — Retain selected potentially relevant consequences.
3. **Allele frequency filtering** — Retain variants with known gnomAD allele frequency ≤ 0.01 and separately record variants with unknown frequency.
4. **CADD prioritization** — Rank variants by CADD score instead of automatically discarding lower-scoring variants.
5. **ClinVar review** — Preserve distinctions among Pathogenic, Likely pathogenic, VUS, conflicting classifications, and other categories.
6. **Inheritance review** — Perform a preliminary review of zygosity and inheritance compatibility.
7. **Summary reporting** — Generate counts and a structured CSV summary.
8. **Visualization** — Plot CADD scores across the candidate variants.
9. **Final candidate table** — Consolidate variant annotations, CADD priority, and inheritance review into one CSV file.

## Final Results

The educational dataset contains 10 synthetic variants.

| Pipeline stage | Variants remaining |
|---|---:|
| Original dataset | 10 |
| After functional consequence filtering | 9 |
| After allele frequency filtering | 7 |
| Final candidate table | 7 |

The final table contains the following information:

- Gene and variant identifier
- Functional consequence
- gnomAD allele frequency
- CADD score
- ClinVar significance
- Zygosity and inheritance model
- SIFT and PolyPhen-2 prediction scores
- CADD priority category
- Preliminary inheritance review

### Final Candidate Variants

**[View the final candidate table](results/final_candidate_variants.csv)**

The final output contains seven candidates. Four have CADD scores ≥ 20, and three have scores < 20. CADD is used as a prioritization aid, not as a standalone clinical classification.

### Other Results

- [Functional variants](results/01_functional_variants.csv)
- [Rare variants](results/02_rare_variants.csv)
- [Variants with unknown frequency](results/02_unknown_frequency.csv)
- [CADD-ranked variants](results/03_cadd_ranked_variants.csv)
- [ClinVar-reviewed candidates](results/04_candidate_variants.csv)
- [Inheritance review](results/05_inheritance_review.csv)
- [Variant summary](results/06_variant_summary.csv)
- [CADD visualization](results/figures/cadd_scores.png)

## Project Structure

```text
WES-Variant-Prioritization/
├── data/
│   └── variants.csv
├── results/
│   ├── 01_functional_variants.csv
│   ├── 02_rare_variants.csv
│   ├── 02_unknown_frequency.csv
│   ├── 03_cadd_ranked_variants.csv
│   ├── 04_candidate_variants.csv
│   ├── 05_inheritance_review.csv
│   ├── 06_variant_summary.csv
│   ├── final_candidate_variants.csv
│   └── figures/
│       └── cadd_scores.png
├── scripts/
│   ├── 01_load_data.py
│   ├── 02_filter_functional.py
│   ├── 03_filter_frequency.py
│   ├── 04_prioritize_cadd.py
│   ├── 05_select_candidates.py
│   ├── 06_inheritance_review.py
│   ├── 07_summary.py
│   ├── 08_cadd_visualization.py
│   └── 09_final_candidate_table.py
└── README.md
```

## Requirements

- Python 3
- pandas
- Matplotlib

Install the required libraries:

```bash
py -m pip install pandas matplotlib
```

## How to Run

Run the scripts from the project root directory in numerical order:

```bash
py scripts/01_load_data.py
py scripts/02_filter_functional.py
py scripts/03_filter_frequency.py
py scripts/04_prioritize_cadd.py
py scripts/05_select_candidates.py
py scripts/06_inheritance_review.py
py scripts/07_summary.py
py scripts/08_cadd_visualization.py
py scripts/09_final_candidate_table.py
```

The scripts write intermediate and final results to the `results/` directory.

## Tools and Skills Demonstrated

- Python scripting and data processing
- pandas DataFrame manipulation and CSV handling
- Variant filtering and prioritization logic
- Missing-value handling
- Population allele frequency interpretation
- CADD score ranking
- ClinVar classification review
- Preliminary zygosity and inheritance checks
- Summary reporting and data visualization
- Reproducible project organization with Git and GitHub

## Limitations

**This project uses synthetic educational data only. It is not a clinical analysis pipeline.**

- The gene names and variant records are fictional examples.
- The workflow demonstrates filtering and prioritization concepts; it does not establish pathogenicity or provide diagnostic conclusions.
- CADD, SIFT, and PolyPhen-2 predictions are supporting evidence, not proof of pathogenicity.
- ClinVar labels are retained as supplied in the dataset and are not independently validated.
- Inheritance compatibility checks are preliminary and do not establish a molecular diagnosis.
- A real WES analysis requires validated annotation, transcript-aware variant interpretation, quality control, phenotype correlation, appropriate inheritance assessment, and expert review.

## Author

**Saba Babaei**

[GitHub Repository](https://github.com/sabababaei1-droid/WES-Variant-Prioritization)
