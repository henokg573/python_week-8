# CORD-19 Data Explorer

## Project Description

This project explores the COVID-19 research dataset (CORD-19) to analyze publication trends, top journals, frequent words in titles, and sources. A simple Streamlit app allows interactive exploration of the dataset.

The project focuses on:
- Loading and exploring a real-world dataset
- Data cleaning and preparation
- Basic data analysis
- Creating visualizations
- Building an interactive Streamlit web application

## Dataset

The project uses the `metadata.csv` file from the CORD-19 dataset, which includes:
- Paper titles and abstracts
- Publication dates
- Authors and journals
- Source information

**Note:** The full dataset is very large; for this assignment, only the metadata file or a subset is required.

Dataset can be downloaded from Kaggle: [CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

## Features

- Display dataset and check for missing values
- Perform data cleaning and preparation
  - Convert publication dates to datetime format
  - Extract publication year
  - Compute abstract word count
- Perform basic analysis
  - Count publications by year
  - Identify top journals
  - Find most frequent words in titles
  - Distribution by source
- Visualizations
  - Bar chart of publications by year
  - Top 10 journals bar chart
  - Word cloud of paper titles
  - Source distribution chart
- Interactive Streamlit app
  - Filter by publication year
  - View top papers
  - Visualize trends interactively

## Installation

Ensure Python 3.7+ is installed and install required packages:

```bash
pip install pandas matplotlib seaborn streamlit wordcloud
```

## Running the Streamlit App

1. Place `cord19_analysis.py` and `metadata.csv` in the same folder.
2. Run the following command in terminal:

```bash
streamlit run cord19_analysis.py
```

3. The app will open in your default browser. You can:
   - Select a publication year range
   - View a table of top papers
   - Explore interactive visualizations

## Project Structure

```
Frameworks_Assignment/
│
├── cord19_analysis.py   # Python script with analysis and Streamlit app
├── metadata.csv         # Dataset file (download separately)
├── README.md            # Project documentation
└── (optional) Notebook.ipynb  # Optional Jupyter Notebook
```

## Key Findings

- Publications have increased significantly from 2019 to 2022.
- Certain journals consistently publish more COVID-19 research.
- Frequent keywords in titles highlight the main focus areas in research.
- The dataset is diverse in terms of sources.

## Author

Henok Girma

## References

- [CORD-19 Dataset on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)