import pandas as pd
import random

# Load the CSV files
first_csv = pd.read_csv('extract_features/datasets/legal_urls.csv')
second_csv = pd.read_csv('extract_features/datasets/combined_dataset.csv')

# Extract the URL columns
first_urls = first_csv['URL'].tolist()
second_urls = set(second_csv['url'].tolist())

# Function to get 20 random URLs not present in second_csv


def get_unique_random_urls(first_urls, second_urls, n=20):
    unique_urls = list(set(first_urls) - second_urls)
    if len(unique_urls) < n:
        raise ValueError("Not enough unique URLs to select from.")
    return random.sample(unique_urls, n)


# Get 20 random unique URLs
random_urls = get_unique_random_urls(first_urls, second_urls)

# Print or save the result
print("Selected URLs:", random_urls)

# Optionally, you can save these URLs to a new CSV file
result_df = pd.DataFrame(random_urls, columns=['url'])
result_df.to_csv('extract_features/datasets/random_urls.csv', index=False)
