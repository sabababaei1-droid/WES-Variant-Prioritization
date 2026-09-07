# WES Variant Prioritization

A Python-based workflow for filtering and prioritizing annotated variants from whole-exome sequencing (WES) data.

## Project Overview

This project demonstrates a reproducible workflow for variant filtering and prioritization using Python and pandas.

The workflow includes:

* Functional variant filtering
* Population frequency filtering
* CADD-based prioritization
* Candidate variant selection based on ClinVar significance
* Summary of filtering results

## Workflow

```text
Annotated WES variants
        ↓
Functional filtering
        ↓
Population frequency filtering
        ↓
CADD prioritization
        ↓
Candidate variant selection
        ↓
Summary of filtering results
```

## Filtering Criteria

The workflow applies the following criteria:

* **Functional consequences:** missense, frameshift, and stop-gained variants
* **Population frequency:** gnomAD allele frequency ≤ 0.01
* **CADD score:** ≥ 20
* **Clinical significance:** ClinVar significance = Pathogenic

## Project Structure

```text
WES-Variant-Prioritization/
├── data/
│   └── variants.csv
├── results/
│   ├── functional_variants.csv
│   ├── rare_variants.csv
│   ├── high_cadd_variants.csv
│   └── candidate_variants.csv
├── scripts/
│   ├── 01_load_data.py
│   ├── 02_filter_functional.py
│   ├── 03_filter_frequency.py
│   ├── 04_prioritize_cadd.py
│   ├── 05_select_candidates.py
│   └── 06_summary.py
└── README.md
```

## Requirements

* Python 3
* pandas

## How to Run

Run the scripts in the following order:

```bash
py scripts/01_load_data.py
py scripts/02_filter_functional.py
py scripts/03_filter_frequency.py
py scripts/04_prioritize_cadd.py
py scripts/05_select_candidates.py
py scripts/06_summary.py
```

The final candidate variants are saved in:

```text
results/candidate_variants.csv
```

The summary script reports the number and percentage of variants remaining after each filtering step.

> This repository is an educational implementation. Patient-level data and unpublished research results are not included.
