import os
import csv
from PIL import Image
import img2pdf

# Set the path to your unzipped folder
base_directory = "/Users/gabbrielmcintosh/Downloads/regsheets"
# Directory to store converted PDF files
output_directory = os.path.join(base_directory, "Converted_PDFs")
# Path to the CSV file for logging
csv_file_path = os.path.join(base_directory, "conversion_log.csv")

# Create the output directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to log file processing into a CSV file
def log_file_processing_to_csv(file_name, status, processed):
    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([file_name, status, processed])

# Convert Files to PDF
def convert_to_pdf(file_path, output_path):
    try:
        if file_path.lower().endswith(('.jpeg', '.jpg', '.png')):
            image = Image.open(file_path)
            pdf_bytes = img2pdf.convert(image.filename, rotation=img2pdf.Rotation.ifvalid)
            with open(output_path, 'wb') as f:
                f.write(pdf_bytes)
            log_file_processing_to_csv(file_name, "Converted to PDF", "Yes")
        elif file_path.lower().endswith('.pdf'):
            # Move the existing PDF to the output directory
            if not os.path.exists(output_path):
                os.rename(file_path, output_path)
                log_file_processing_to_csv(file_name, "Moved PDF to output directory", "Yes")
            else:
                log_file_processing_to_csv(file_name, "PDF already exists in output directory", "Yes")
    except img2pdf.ExifOrientationError:
        log_file_processing_to_csv(file_name, "Invalid rotation", "No")
    except Exception as e:
        log_file_processing_to_csv(file_name, f"Error: {e}", "No")

# Initialize the CSV file with headers
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["File Name", "Status", "Processed"])

# Main script logic
files = os.listdir(base_directory)

for file_name in files:
    file_path = os.path.join(base_directory, file_name)
    pdf_name = os.path.splitext(file_name)[0] + '.pdf'
    pdf_path = os.path.join(output_directory, pdf_name)
    
    if file_name.lower().endswith(('.jpeg', '.jpg', '.png', '.pdf')):
        # Convert or move files
        convert_to_pdf(file_path, pdf_path)
    else:
        log_file_processing_to_csv(file_name, "Unsupported file type", "No")

# Final check to verify processing
total_processed_files = len(os.listdir(output_directory))
log_file_processing_to_csv("Total processed files", total_processed_files, "N/A")
print(f"Total files in Converted_PDFs folder: {total_processed_files}")
print(f"Expected total: {len(files)}")

if total_processed_files != len(files):
    print("Warning: Some files may not have been processed correctly. Check the log for details.")
