import pandas as pd

def convert_txt_to_csv():
    # Read the text file with URLs
    file_path = 'extract_features/datasets/legal_urls.txt'
    with open(file_path, 'r') as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls]  # Remove any trailing newline characters

    # Convert the list of URLs into a DataFrame
    df = pd.DataFrame(urls, columns=['URL'])

    # Save the DataFrame to a CSV file
    csv_file_path = 'extract_features/datasets/legal_urls.csv'
    df.to_csv(csv_file_path, index=False)

    return csv_file_path