# cord19_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

sns.set(style="whitegrid")

# --- Part 1: Data Loading ---
try:
    df = pd.read_csv('metadata.csv')
    st.write("Data loaded successfully!")
except FileNotFoundError:
    st.error("File not found. Please place 'metadata.csv' in the working directory.")

# Basic exploration
print("Dataset shape:", df.shape)
print(df.info())
print(df.isnull().sum())
display(df.head())

# --- Part 2: Data Cleaning ---
# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Drop rows without publish_time
df = df.dropna(subset=['publish_time'])

# Create year column
df['year'] = df['publish_time'].dt.year

# Create abstract word count column
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# --- Part 3: Data Analysis and Visualization ---
# Papers by year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.show()

# Top journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis')
plt.title('Top 10 Journals by Number of Publications')
plt.xlabel('Number of Papers')
plt.show()

# Word cloud of titles
all_titles = " ".join(df['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.show()

# Distribution by source
source_counts = df['source_x'].value_counts()
plt.figure(figsize=(8,5))
sns.barplot(x=source_counts.index, y=source_counts.values, palette='magma')
plt.title('Publications by Source')
plt.ylabel('Number of Papers')
plt.show()

# --- Part 4: Streamlit App ---
st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Year range slider
year_min = int(df['year'].min())
year_max = int(df['year'].max())
selected_years = st.slider("Select publication year range", year_min, year_max, (year_min, year_max))

filtered_df = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]

st.write(f"Number of papers in selected range: {filtered_df.shape[0]}")
st.dataframe(filtered_df[['title','authors','journal','year']].head(20))

# Plot publications over time for selected range
year_counts_filtered = filtered_df['year'].value_counts().sort_index()
st.bar_chart(year_counts_filtered)
