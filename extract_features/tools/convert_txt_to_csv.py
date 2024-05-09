import pandas as pd

def convert_txt_to_csv():
    # Step 1: Read the text file with URLs
    file_path = 'extract_features/datasets/legal_urls.txt'  # Change this to the path of your text file
    with open(file_path, 'r') as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls]  # Remove any trailing newline characters

    # Step 2: Convert the list of URLs into a DataFrame
    df = pd.DataFrame(urls, columns=['URL'])

    # Step 3: Save the DataFrame to a CSV file
    csv_file_path = 'extract_features/datasets/legal_urls.csv'  # Change this to your desired output file name
    df.to_csv(csv_file_path, index=False)

    return csv_file_path