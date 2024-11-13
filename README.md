# CRITRseq_Interferon_Flu

This repository contains the code used to analyze data from a genome-wide CRITR-seq screen for modulators of interferon induction by influenza A virus. It also includes code used to analyze follow-up experiments on the top hits from the screen, as well as the code used to generate figures.

Analyses are found in different Jupyter notebooks, with descriptions below. Figures generated can be seen in the Jupyter notebooks.

The Data folder in this repository includes all qPCR csv files. Sequencing files can be downloaded from ___ at accession ___.

## Directories

This repository contains the following directories:
- <b>CRITR-seq_SequencingAnalysis</b> Includes the following files:
  - csv files with gRNAs from Genome-scale CRISPR Knockout (GeCKO) v2 libraries A and B (Addgene #1000000048, #1000000049).
  - Assign_Barcodes.ipynb contains code that (1) assigns reads from the sequencing FASTA files to gRNA barcodes and (2) generates counts files to input for analysis with Model-based Analysis of Genome-wide CRISPR/Cas9 Knockout (MAGeCK).
  - MAGeCK_Analysis.ipynb contains code for data visualization after MAGeCK analysis.
  - Sequencing directory contains counts files generated from the plamsid, genomic DNA, and mRNA sequencing performed for the CRITR-seq screen in this study, using the code in Assign_Barcodes.ipynb.
- <b>Data</b> qPCR data

## Dependencies

The following python packages and versions were used. All were installed using conda. (https://docs.conda.io/en/latest/)
- <b>json</b> run with version 2.0.9. (https://www.json.org/)
- <b>numpy</b> run with version 1.26.4. (https://numpy.org/).
- <b>matplotlib</b> run with version 3.8.4 (https://matplotlib.org/).
- <b>seaborn</b> run with version 0.13.2 (https://seaborn.pydata.org/).
- <b>pandas</b> run with version 2.2.1 (https://pandas.pydata.org/).
- <b>scipy</b> run with version 1.13.0 (https://www.scipy.org/).
- <b>statsmodels</b> run with version 0.14.1 (https://www.statsmodels.org/stable/index.html).

Model-based Analysis of Genome-wide CRISPR/Cas9 Knockout (MAGeCK) (https://sourceforge.net/projects/mageck/) was run with version 0.5.9.5.

## Jupyter Notebooks

General descriptions of pipelines within each notebook are described below.

### CapLength_Analysis.ipynb

Analysis of 5' RACE sequencing data from flu mRNAs, with or without siRNA targeting *NELFB*.

### Flow_Analysis.ipynb

Analysis of flow cytometry data, after initial gate to exclude debris was drawn in FlowJo and the data were exported to csv files. Thresholds for interferon positivity and influenza A protein staining were set on uninfected controls, expected to have no production of interferons or staining for flu proteins.

### qPCR_Analysis.ipynb

Analysis of qPCR data exported to csv files.

### Assign_Barcodes.ipynb

### MAGeCK_Analysis.ipynb
