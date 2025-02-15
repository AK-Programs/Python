# Password Protection for File Access

# This script provides a simple password protection mechanism for accessing a file. 
# It prompts the user to create a password if one does not exist, and then uses that 
# password to control access to a specified file.
# Usage:
# 1. Run the script.
# 2. If no password exists, you will be prompted to create one.
# 3. After setting the password, you will be asked to provide the path to the file you want to protect.
# 4. On subsequent runs, you will need to enter the password to access the protected file.
# Make sure:
# - The file paths provided are correct and accessible.
# - You have created a password data file named 'password.txt' in the same folder where the Python file is located.
# Function:
# protected_file() : Manages password creation and verification, and controls access to a specified file.
# open_and_read_file(file_path) : Opens and reads the content of the specified file.
# main() : Entry point of the program, displays a welcome message and calls the protected_file() function.
# Note: This script is a basic example and may not provide strong security. For more secure implementations, consider using encryption and hashing techniques.
    
import os  

def protected_file():  
    
    # Check if the password file exists and read the password  
    if os.path.exists("password.txt"):  
        f = open("password.txt", "r")  
        password = f.readline().strip()  
        f.close()  
    else:  
        password = ""  

    if password == "":  
        # No password exists: prompt to create one  
        create = input("Create a password: ").strip()  
        confirm = input("Confirm your password: ").strip()  
        
        if create == confirm:  
            print("Your password has been set.")  
            # Save the new password  
            f = open("password.txt", "w")  
            f.write(confirm)  
            f.close()  

            # Ask for the file path after setting up the password  
            file_path = input("Enter the path of the file: ").strip()  
            f = open("file_path.txt", "w")  # Save the file path  
            f.write(file_path)  
            f.close()  
            
            print("Protecting File...")
            print("Your file is protected.")  
            open_and_read_file(file_path)  # Read the file content  
        else:  
            print("The passwords do not match.")  
    else:  
        # Existing password: prompt for it  
        confirm = input("Enter the password: ").strip()  
        if confirm == password:  
            print("Accessing file...")
            print("Access granted.")  
            
            f = open("file_path.txt", "r")  
            file_path = f.readline().strip()  
            f.close()  

            open_and_read_file(file_path)  
        else:  
            print("Incorrect password.")
            print("Access denied.")  

def open_and_read_file(file_path):  
    if os.path.exists(file_path):
        f = open(file_path, "r")  
        print(f.read())  
        f.close()  
    else:  
        print("File does not exist: ", file_path)  

def main():
    print("Welcome to the password-protected file program.")
    protected_file()
    
main()
