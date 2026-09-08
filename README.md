# WES Variant Prioritization

A Python-based workflow for filtering and prioritizing annotated variants from whole-exome sequencing (WES) data.

## Project Overview

This project demonstrates a reproducible workflow for variant filtering and prioritization using Python, pandas, and Matplotlib.

The workflow includes:

* Functional variant filtering
* Population frequency filtering
* CADD-based prioritization
* Candidate variant selection based on ClinVar significance
* Summary of filtering results
* CADD score visualization

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
        ↓
CADD visualization
```

## Filtering Criteria

The workflow applies the following criteria:

* **Functional consequences:** missense, frameshift, and stop-gained variants
* **Population frequency:** gnomAD allele frequency ≤ 0.01
* **CADD score:** ≥ 20
* **Clinical significance:** ClinVar significance = Pathogenic

## CADD Visualization

The project includes a Python script for visualizing CADD scores of prioritized variants.

The visualization includes:

* CADD score for each prioritized variant
* A horizontal threshold line at CADD = 20
* Numerical labels for individual CADD scores
* High-resolution PNG output

The visualization script is:

```text
scripts/07_cadd_visualization.py
```

The script uses Matplotlib to generate the visualization.

> The patient-level input file used to generate the visualization is not included in this repository.

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
│   ├── 06_summary.py
│   └── 07_cadd_visualization.py
└── README.md
```

## Requirements

* Python 3
* pandas
* Matplotlib
* openpyxl

Install the required Python packages with:

```bash
py -m pip install pandas matplotlib openpyxl
```

## How to Run

Run the main filtering workflow in the following order:

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

The CADD visualization can be generated using:

```bash
py scripts/07_cadd_visualization.py
```

> The visualization script requires the corresponding local input Excel file. Patient-level data are not included in this repository.

## Data Privacy

Patient-level data and unpublished research results are not included in this repository.

The files used for patient-specific analysis remain local and are not uploaded to GitHub.

> This repository is an educational implementation demonstrating a reproducible approach to variant filtering, prioritization, and visualization using Python.
