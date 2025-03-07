# Simple File Organizer

# This script organizes files in a specified directory into subdirectories based on their file extensions.
# For example, all .txt files will be moved to a subdirectory named TXT_FILES, all .jpg files will be moved to JPG_FILES, and so on.
# Files without an extension will be skipped.
# The user is prompted to enter the directory path they want to organize.

import os  
import shutil  
import time

def organize_files(directory):  

    for filename in os.listdir(directory):  
        if os.path.isfile(os.path.join(directory, filename)):  # Ensure it's a file  
            base, ext = os.path.splitext(filename)  
            ext = ext.lstrip(".")  # Remove the leading dot  
            if ext: # Only process if there's an extension  
                target_dir = os.path.join(directory, ext.upper() + "_FILES")    # Create a dir named EXTENSION_FILES  
                targeted_file = os.path.basename(target_dir)
                if not os.path.exists(target_dir):  
                    os.makedirs(target_dir)  
                shutil.move(os.path.join(directory, filename), os.path.join(target_dir, filename))  
                print(f"Organizing {filename}...")
                time.sleep(2)
                print(f"Moved {filename} to {targeted_file} directory.")  
            else:  
                print(f"Skipped file with no extension: {filename}")  

# Get the directory from user  
print("Welcome to the File Organizer")
directory_path = input("Enter the directory to organize: ")  
print("Analyzing files in the directory...")
time.sleep(2)

# Organize  
organize_files(directory_path)  
print("Almost done...")
time.sleep(2)
print("File organization complete.")  
print("Thank you for using the File Organizer.")