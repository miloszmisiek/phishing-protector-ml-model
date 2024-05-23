import pandas as pd

# Load the CSV file into a DataFrame
csv_file_path = 'extract_features/datasets/combined_dataset.csv'
df = pd.read_csv(csv_file_path)

total_count = len(df)

# Count the records where the phishing column is 1
phishing_count = len(df[df["phishing"] == 0])

print(f'The number of records classified as phishing is: {phishing_count}, out of a total of {total_count} records.')
