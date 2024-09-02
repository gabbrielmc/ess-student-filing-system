# ess-student-filing-system

## Project Overview

This project automates the conversion, organization, and verification of student registration sheet files. It ensures that all files are correctly formatted as PDFs and stored in well-organized subfolders.

### Key Features:
- **Conversion:** Automatically converts image files (JPEG, PNG) to PDF format.
- **Organization:** Places the PDFs in subfolders based on the student's last name and ID.
- **Verification:** Checks that all files have been correctly processed and organized.

### Language & Libraries:
- **Language:** Python
- **Libraries Used:**
  - `PIL`: For image handling and conversion.
  - `img2pdf`: Converts images to PDF format.
  - `csv`: Manages the logging of processed files.
  - `os`, `shutil`: Handles file and directory operations.

## Installation Instructions

To get started, install the required Python libraries:

```bash
pip install pillow img2pdf
```

## File Descriptions

- **`file_converter.py`**  
  Converts image files (JPEG, PNG) to PDF and moves existing PDF files to a designated folder. It also logs the status of each file.

- **`file_converter_checker.py`**  
  Compares the original folder with the converted files folder to ensure all files were processed correctly.

- **`organize_files.py`**  
  Organizes the converted PDF files into subfolders based on the first letter of the last name and further into subfolders named with the student's full name and ID.

- **`organization_checker.py`**  
  Verifies that the organized folder matches the original folder in terms of file count and names, ensuring every file is correctly organized.

## How to Use

1. **Place Files:** Put all the files to be processed in the `regsheets` directory.
2. **Convert Files:** Run `file_converter.py` to convert images to PDFs and move the files.
3. **Verify Conversion:** Run `file_converter_checker.py` to ensure all files were converted successfully.
4. **Organize Files:** Run `organize_files.py` to sort the converted files into the appropriate subfolders.
5. **Check Organization:** Run `organization_checker.py` to verify that all files are correctly organized.

## Logs

Logs for file conversion and organization are stored in the same directory as the original files (`regsheets`). These CSV logs include the status of each file, noting any errors or unprocessed files.
