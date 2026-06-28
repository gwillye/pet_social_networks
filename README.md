# Social Media & Well-Being — Correlation Study (PET Sistemas / UFMS)

> **Real-world context.** Research conducted at **PET Sistemas (UFMS)**, which produced a scientific article on the **impact of social media on Computer Science students**. This repository is the **data-science / statistics pipeline** behind it: psychometric factor scoring, data cleaning, and correlation analysis between social-media usage and well-being scales.

A reproducible pipeline that scores the **QSG-12 (General Health Questionnaire)** into well-being **factors** (Anxiety, Depression, Self-efficacy), processes a **social-media impact scale (EAISR-E)**, and measures their association with **Pearson / Spearman / Kendall** correlations — broken down by student segment (course, gender, age, course stage, GPA).

## 🔬 Methodology
1. **Cleaning** (`data-processing/`): strip personal identifiers (`filtrar_dados_pessoais.py`), isolate each instrument (`filtrar_qsg12.py`, `filtrar_eaisre.py`), word/answer counts.
2. **Factor scoring** (`analysis/fatores_2.py`): compute the QSG-12 factors with correct **reverse-scoring** of negative items → Anxiety, Depression, Self-efficacy.
3. **Correlation** (`analysis/correlacao_final_*.py`): Pearson correlation (coefficient + p-value) between each EAISR-E item and each QSG-12 factor; partitioned variants for segmented analysis.
4. **Segmentation** (`analysis/particionar_datasets.py`, `reestruturar_dados.py`): split the sample by course, gender, age band, course stage and GPA, then recompute correlations per segment.

## 📊 Results
`results/pearson-by-segment/` holds the **aggregate correlation tables** (coefficient + p-value) per segment — e.g. `Ciência da Computação`, `Engenharia de Software`, `homens`/`mulheres`, `idade_sub21` … `idade_over27`, `inicio_curso`/`fim_curso`, `over_mga`. These are aggregate statistics only — no individual responses.

## 🔒 Data & ethics
The **raw psychometric responses are not included.** They are sensitive individual data (mental-health screening), so only the **code (methodology)** and the **aggregate correlation results** are published. To reproduce end-to-end, supply your own response files (the expected filenames are listed in `.gitignore`).

## 🛠️ Stack
Python · pandas · SciPy (`pearsonr`) · CSV / SQLite

## 📁 Structure
```
pet-social-networks/
├── data-processing/          # cleaning, anonymization, scoring inputs
├── analysis/                 # factor scoring + correlation (final version)
└── results/
    └── pearson-by-segment/   # aggregate correlation tables per segment
```
