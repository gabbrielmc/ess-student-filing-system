import os
import csv

# Paths to the original and organized folders
original_folder = "/Users/gabbrielmcintosh/Downloads/regsheets"
organized_folder = "/Users/gabbrielmcintosh/Downloads/new"

# Function to get a list of all files in a folder and its subfolders, ignoring extensions
def get_all_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            # Use os.path.splitext to ignore file extensions for comparison
            base_name = os.path.splitext(file)[0]
            file_list.append(os.path.relpath(os.path.join(root, file), directory))
    return file_list

def get_base_names(files):
    return {os.path.splitext(os.path.basename(file))[0] for file in files}

# Get lists of files
original_files = get_all_files(original_folder)
organized_files = get_all_files(organized_folder)

# Extract base names for comparison
original_base_names = get_base_names(original_files)
organized_base_names = get_base_names(organized_files)

# Compare lists
missing_files = original_base_names - organized_base_names
extra_files = organized_base_names - original_base_names

# Print results
if not missing_files and not extra_files:
    print("All matches found. Every file is accounted for and correctly organized.")
else:
    if missing_files:
        print(f"Missing files: {len(missing_files)}")
    if extra_files:
        print(f"Extra files: {len(extra_files)}")

# Save the report to a CSV file
with open('/Users/gabbrielmcintosh/Downloads/comparison_report.csv', 'w', newline='') as csvfile:
    fieldnames = ['File Name', 'Status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for file in missing_files:
        writer.writerow({'File Name': file, 'Status': 'Missing'})
    
    for file in extra_files:
        writer.writerow({'File Name': file, 'Status': 'Extra'})
