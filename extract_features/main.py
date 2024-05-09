import asyncio
import pandas as pd
from extract_features.tools.convert_txt_to_csv import convert_txt_to_csv
from extract_features.tools.extract_features import extract_features
import random


async def extract_features_for_all(urls: list):
    tasks = [extract_features(url) for url in urls]
    return await asyncio.gather(*tasks)


async def main():
    phishing_pd = pd.read_csv('extract_features/datasets/verified_online.csv')
    legals_pd = pd.read_csv(convert_txt_to_csv())

    phishing_urls = phishing_pd['url'].tolist()
    legals_urls = legals_pd['URL'].tolist()
    phishing_urls_to_process = random.sample(phishing_urls, 3000)
    legals_urls_to_process = random.sample(legals_urls, 3000)

    phishing_feature_data = await extract_features_for_all(phishing_urls_to_process)
    legals_feature_data = await extract_features_for_all(legals_urls_to_process)
    phishing_features_df = pd.DataFrame(phishing_feature_data)
    legals_features_df = pd.DataFrame(legals_feature_data)

    phishing_features_df['phishing'] = 1  # Mark as phishing
    legals_features_df['phishing'] = 0    # Mark as legal

    # Concatenate phishing and legal dataframes
    features_df = pd.concat(
        [phishing_features_df, legals_features_df], ignore_index=True)

    # Randomize the rows of the DataFrame
    features_df = features_df.sample(frac=1).reset_index(drop=True)

    # Save the combined and randomized DataFrame to CSV
    features_df.to_csv(
        'extract_features/datasets/combined_dataset.csv', index=False)

if __name__ == '__main__':
    asyncio.run(main())  # Run the async function
