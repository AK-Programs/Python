# File Renamer

# This script renames a file if it exists in the current directory.
# It checks if the source file exists, and if it does, renames it to the destination file name.
# If the source file does not exist, it prints an error message.
# If you want to convert a txt file to a python file, you can use this script to rename the file or any other file extension.
# Make sure to replace sample.ext with the actual file name and extension.
# Make sure if you are renaming a txt file to a python file, the file content is valid Python code or you may encounter errors.


import os  

source_file = "sample.ext"  
destination_file = "sample.ext"  

if os.path.exists(source_file):  
    os.rename(source_file, destination_file)  
    print(f"Renamed {source_file} to {destination_file}")  
else:  
    print(f"{source_file} does not exist.")