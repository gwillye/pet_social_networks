# Social Media and Well-Being: A Correlation Study (PET Sistemas / UFMS)

This repository holds the data-science and statistics pipeline behind a research project carried out at PET Sistemas (UFMS). The group produced a scientific article on the impact of social media on Computer Science students, and the code here is what powers the analysis: psychometric factor scoring, data cleaning, and correlation analysis between social-media usage and well-being scales.

## What it does

The pipeline scores the QSG-12 (General Health Questionnaire) into well-being factors (Anxiety, Depression, Self-efficacy), processes a social-media impact scale (EAISR-E), and measures how the two relate using Pearson, Spearman, and Kendall correlations. Results are broken down by student segment: course, gender, age, course stage, and GPA.

## How it works

1. Cleaning (`data-processing/`): strip personal identifiers (`filtrar_dados_pessoais.py`), isolate each instrument (`filtrar_qsg12.py`, `filtrar_eaisre.py`), and compute word/answer counts.
2. Factor scoring (`analysis/fatores_2.py`): compute the QSG-12 factors with correct reverse-scoring of negative items, producing Anxiety, Depression, and Self-efficacy.
3. Correlation (`analysis/correlacao_final_*.py`): Pearson correlation (coefficient plus p-value) between each EAISR-E item and each QSG-12 factor, with partitioned variants for segmented analysis.
4. Segmentation (`analysis/particionar_datasets.py`, `reestruturar_dados.py`): split the sample by course, gender, age band, course stage, and GPA, then recompute correlations per segment.

## Results

`results/pearson-by-segment/` holds the aggregate correlation tables (coefficient plus p-value) for each segment, for example `Ciência da Computação`, `Engenharia de Software`, `homens`/`mulheres`, `idade_sub21` through `idade_over27`, `inicio_curso`/`fim_curso`, and `over_mga`. These are aggregate statistics only, with no individual responses.

## Data and ethics

The raw psychometric responses are not included. They are sensitive individual data (mental-health screening), so only the code (the methodology) and the aggregate correlation results are published. To reproduce the analysis end to end, you need to supply your own response files. The expected filenames are listed in `.gitignore`.

## Stack

Python, pandas, SciPy (`pearsonr`), CSV / SQLite.

## Structure

```
pet-social-networks/
├── data-processing/          # cleaning, anonymization, scoring inputs
├── analysis/                 # factor scoring + correlation (final version)
└── results/
    └── pearson-by-segment/   # aggregate correlation tables per segment
```
