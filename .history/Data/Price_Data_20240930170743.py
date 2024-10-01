import os
import zipfile

# Specify the folder path containing the zip files
zip_folder = r'C:\Users\achra\Downloads\Ercot_Price_Data'
output_folder = r'C:\Users\achra\Downloads\Ercot_Price_Data_Extracted'

# Create an output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over all files in the folder
for filename in os.listdir(zip_folder):
    if filename.endswith('.zip'):  # Check if the file is a zip file
        zip_path = os.path.join(zip_folder, filename)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract contents to the output folder
            zip_ref.extractall(output_folder)
        print(f"Extracted: {filename}")

print("All files have been extracted successfully.")
