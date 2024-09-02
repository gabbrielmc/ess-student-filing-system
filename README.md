# ess-student-filing-system
1. Project Overview

Purpose: The project automates the conversion, organization, and verification of student registration sheet files, ensuring they are in the correct format (PDF) and stored in organized subfolders.

Language: Python

Libraries Used:
- PIL: Used for image handling and conversion.
- img2pdf: Converts images to PDF format.
- csv: Handles the logging of processed files.
- os, shutil: Manages file and directory operations.

2. Installation Instructions

Install the required Python libraries:
- pip install pillow img2pdf

3. File Descriptions
file_converter.py: Converts image files (JPEG, PNG) to PDF and moves existing PDF files to a designated folder. Logs the status of each file.

file_converter_checker.py: Compares the original folder with the converted files folder to ensure all files were processed correctly.

organize_files.py: Organizes the converted PDF files into subfolders based on the first letter of the last name, and further into subfolders named with the student's full name and ID.

organization_checker.py: Verifies that the organized folder matches the original folder in terms of file count and names, ensuring every file is correctly organized.

4. How to Use
Place all the files to be processed in the regsheets directory.
Run file_converter.py to convert and move the files.
Run file_converter_checker.py to verify the conversion.
Run organize_files.py to organize the converted files into subfolders.
Run file_organization_checker.py to verify that all files are correctly organized.

5. Logs
Logs for file conversion and organization are stored in the same directory as the original files (regsheets).

The CSV logs include the status of each file, noting any errors or unprocessed files.
