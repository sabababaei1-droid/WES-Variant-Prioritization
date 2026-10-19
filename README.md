# WES Variant Prioritization

A Python-based educational workflow for prioritizing annotated genetic variants from whole-exome sequencing (WES) data.

## Project Overview

This project demonstrates a reproducible variant prioritization workflow using **Python, pandas, and Matplotlib**. It uses a synthetic dataset to illustrate how functional consequences, population allele frequency, ClinVar classifications, CADD scores, zygosity, and inheritance patterns can be organized for candidate review.

## Workflow

1. **Load and validate data** — Check required columns and annotation data types.
2. **Functional consequence filtering** — Retain selected potentially relevant consequences.
3. **Allele frequency filtering** — Separate rare variants, common variants, and variants with unknown frequency.
4. **CADD prioritization** — Rank variants by CADD score rather than automatically discarding lower-scoring variants.
5. **ClinVar review** — Keep classifications such as Pathogenic, Likely pathogenic, VUS, and conflicting classifications distinct.
6. **Inheritance review** — Perform a preliminary review of zygosity and inheritance compatibility.
7. **Summary reporting** — Generate counts and a structured CSV summary.
8. **Visualization** — Plot CADD scores across the educational variants.

## Project Structure

```text
WES-Variant-Prioritization/
├── data/
│   └── variants.csv
├── results/
│   └── figures/
├── scripts/
│   ├── 01_load_data.py
│   ├── 02_filter_functional.py
│   ├── 03_filter_frequency.py
│   ├── 04_prioritize_cadd.py
│   ├── 05_select_candidates
