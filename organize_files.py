import os
import shutil

# Path to the main folder where files are located
base_directory = "path to reg sheets"

# Function to extract the last name from the file name
def extract_last_name(file_name):
    try:
        name_part = file_name.split(' ')[0]
        last_name = name_part.split(',')[0].strip()
        return last_name[0].upper()  # Return the first letter of the last name, capitalized
    except Exception as e:
        print(f"Error extracting last name from file {file_name}: {e}")
        return None

# Create letter folders
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in letters:
    letter_folder = os.path.join(base_directory, letter)
    if not os.path.exists(letter_folder):
        os.makedirs(letter_folder)

# Organize files
files = [f for f in os.listdir(base_directory) if os.path.isfile(os.path.join(base_directory, f))]
for file_name in files:
    file_path = os.path.join(base_directory, file_name)
    
    last_name_letter = extract_last_name(file_name)
    if last_name_letter:
        letter_folder = os.path.join(base_directory, last_name_letter)
        if not os.path.exists(letter_folder):
            os.makedirs(letter_folder)

        # Extract full name and ID for subfolder
        try:
            full_name = file_name.split('_')[0]
            subfolder_name = file_name.split('.')[0]  # Remove file extension for subfolder name
            subfolder_path = os.path.join(letter_folder, subfolder_name)
            
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
            
            # Move the file to the appropriate subfolder
            shutil.move(file_path, os.path.join(subfolder_path, file_name))
            print(f"Moved {file_name} to {subfolder_path}")
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

print("Organization complete.")
