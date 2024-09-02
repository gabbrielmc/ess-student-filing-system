import os
import csv

# Set the paths
original_folder = "/Users/gabbrielmcintosh/Downloads/regsheets"
converted_folder = os.path.join(original_folder, "Converted_PDFs")
comparison_csv_path = os.path.join(original_folder, "comparison_log.csv")

# Get the list of files in the original and converted folders
original_files = [os.path.splitext(file)[0] for file in os.listdir(original_folder) if file.lower().endswith(('.jpeg', '.jpg', '.png', '.pdf'))]
converted_files = [os.path.splitext(file)[0] for file in os.listdir(converted_folder)]

# Find the missing files
missing_files = set(original_files) - set(converted_files)

# Write the comparison results to a CSV file
with open(comparison_csv_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["File Name", "Status"])
    
    for file_name in original_files:
        if file_name in converted_files:
            writer.writerow([file_name, "Converted/Processed"])
        else:
            writer.writerow([file_name, "Missing"])

# Output the results
print(f"Comparison complete. Missing files logged in {comparison_csv_path}")
if missing_files:
    print(f"Missing files: {len(missing_files)}")
else:
    print("All files were successfully processed.")
