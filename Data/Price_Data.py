import os
import zipfile
import pandas as pd

# Specify the folder paths
zip_folder = r'C:\Users\achra\Downloads\Ercot_Price_Data'
output_folder = r'C:\Users\achra\Downloads\Final_ERCOT_Energy_Prices'
final_csv = os.path.join(output_folder, "Final_ERCOT_Energy_Prices.csv")

# Create a new folder for the final dataset if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder, exist_ok=True)
    print(f"Created folder: {output_folder}")
else:
    print(f"Folder '{output_folder}' already exists. Skipping creation.")

# Check if the extracted folder exists, extract if it does not
extracted_folder = r'C:\Users\achra\Downloads\Ercot_Price_Data_Extracted'
if not os.path.exists(extracted_folder):
    os.makedirs(extracted_folder, exist_ok=True)
    for filename in os.listdir(zip_folder):
        if filename.endswith('.zip'):
            zip_path = os.path.join(zip_folder, filename)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extracted_folder)
            print(f"Extracted: {filename}")
else:
    print(f"Folder '{extracted_folder}' already exists. Skipping extraction.")

# Merge all CSV files into one inside the final folder, if the output CSV does not already exist
if not os.path.exists(final_csv):
    csv_files = [f for f in os.listdir(extracted_folder) if f.endswith('.csv')]
    if csv_files:
        merged_data = pd.concat([pd.read_csv(os.path.join(extracted_folder, f)) for f in csv_files])
        merged_data.to_csv(final_csv, index=False)
        print(f"All CSV files have been merged into '{final_csv}'.")
    else:
        print("No CSV files found to merge.")
else:
    print(f"The merged CSV file '{final_csv}' already exists. Skipping merge.")
