import pandas as pd

def convert_xlsx_to_csv(xlsx_file, csv_file):
    try:
        # Read the XLSX file
        df = pd.read_excel(xlsx_file)

        # Write to CSV file
        df.to_csv(csv_file, index=False)

        print("Conversion successful!")
    except Exception as e:
        print("An error occurred during conversion:", str(e))

# Define file paths
xlsx_file = "/path/to/input.xlsx"
csv_file = "/path/to/output.csv"

# Convert XLSX to CSV
convert_xlsx_to_csv(xlsx_file, csv_file)
