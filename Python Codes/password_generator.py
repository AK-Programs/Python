# Password Generator

# This script is a Password Generator that allows users to create a custom password.
# Users can choose to include alphabets, numbers, and special characters in their password.
# The script will prompt the user for the number of each type of character to include.
# The generated password will be displayed to the user, and they can choose to generate another password if desired.

import random  
import time

def password_generator():
    while True:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        special_characters = "!@#$%^&*()"
        password = ""
        
        add_alphabets = input("Do you want to add alphabets in your password? (yes/no): ")
        if add_alphabets.lower() == "yes":
            how_many_alpha = int(input("How many alphabets do you want to add? "))
            while how_many_alpha > 10:
                print("Please enter a number less than 10")
                how_many_alpha = int(input("How many alphabets do you want to add? "))
                
            for i in range(how_many_alpha):
                password += random.choice(alphabets)
                
        add_numbers = input("Do you want to add numbers in your password? (yes/no): ")
        if add_numbers.lower() == "yes":
            how_many_numbers = int(input("How many numbers do you want to add? "))
            while how_many_numbers > 10:
                print("Please enter a number less than 10")
                how_many_numbers = int(input("How many numbers do you want to add? "))
        
            for i in range(how_many_numbers):
                password += random.choice(numbers)
                
        add_special_characters = input("Do you want to add special characters in your password? (yes/no): ")
        if add_special_characters.lower() == "yes":
            how_many_special_characters = int(input("How many special characters do you want to add? "))
            while how_many_special_characters > 10:
                print("Please enter a number less than 10")
                how_many_special_characters = int(input("How many special characters do you want to add? "))
                
            for i in range(how_many_special_characters):
                password += random.choice(special_characters)
        
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)
        if password == "":
            print("Please select at least one option to generate a password.")
            password_generator()
            
        time.sleep(1)
        print("Generating password...")
        time.sleep(2)    
        print(f"Your password is: {password}")
        
        again = input("Do you want to generate another password? (yes/no): ")
        if again.lower() == "yes":
            password_generator()
        else:
            print("Thank you for using the Password Generator!")
            break

def main():
    print("Welcome to the Password Generator!")
    password_generator()
    
main()