# WES Variant Prioritization

A Python-based workflow for filtering and prioritizing annotated variants from whole-exome sequencing (WES) data.

## Project Overview

This project demonstrates a reproducible workflow for variant filtering and prioritization using Python.

The workflow includes:

* Functional variant filtering
* Population frequency filtering
* CADD-based prioritization
* Candidate variant selection

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
```

## Filtering Criteria

The workflow applies the following criteria:

* **Functional consequences:** missense, frameshift, and stop-gained variants
* **Population frequency:** gnomAD allele frequency ≤ 0.01
* **CADD score:** ≥ 20

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
│   └── 05_select_candidates.py
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
```

The final candidate variants are saved in:

```text
results/candidate_variants.csv
```

> This repository is an educational implementation. Patient-level data and unpublished research results are not included.
