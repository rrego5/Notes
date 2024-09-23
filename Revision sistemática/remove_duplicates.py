import pandas as pd

# Load the CSV files
file_paths = ['psychinfo_medline.csv', 'psychinfo.csv', 'PubMed.csv', 'scopus.csv', 'ieee.csv']

# Read the CSV files into DataFrames and concatenate them into a single DataFrame
df_list = [pd.read_csv(file_path) for file_path in file_paths]
df_combined = pd.concat(df_list, ignore_index=True)

# Normalize the DOI by ensuring they are strings and removing any leading/trailing spaces
df_combined['DOI'] = df_combined['DOI'].astype(str).str.strip()

# Drop duplicate DOIs, keeping only unique entries
df_unique = df_combined.drop_duplicates(subset='DOI', keep=False)

# Save the unique rows to a new CSV file for review
df_unique.to_csv('unique_articles.csv', index=False)

# Output the number of unique rows found
print(f"Number of unique rows: {len(df_unique)}")
print("Unique rows have been saved to 'unique_articles.csv'")
