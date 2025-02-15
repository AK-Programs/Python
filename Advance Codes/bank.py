# Banking Program

# This program simulates a simple banking system where users can check their balance, withdraw funds, and deposit funds.
# The balance is stored in 'bank_data.txt' in the same directory as the script.
# Functions:
#     balance(): Reads and displays the current balance.
#     withdraw(): Withdraws an amount and updates the balance.
#     deposit(): Deposits an amount and updates the balance.
#     main(): Provides a menu for user interaction.
# Usage:
#     Ensure the name of bank data file named 'bank_data.txt' and make sure to write "Balance: 0" before you run the code.

def balance():  
    f = open("bank_data.txt", "r")  
    line = f.readline().strip()  
    f.close()   

    if line.startswith("Balance:"):  
        balance = line.split(":")[1].strip()
        
        if balance:  
            float_balance = float(balance[1:]) 
            
            print(f"Balance: ${float_balance:.2f}")  
        else:  
            print("Error: The balance value is empty.")  
    else:  
        print("Error: The line does not start with 'Balance:'")  
        
def withdraw():
    show_balance = open("bank_data.txt", "r")
    line = show_balance.readline().strip()
    print(f"Your current balance is ${line.split(': $')[1]}")
    show_balance.close()
    withdraw_amount = input("Enter the amount you want to withdraw: $")
    f = open("bank_data.txt", "r")
    line = f.readline().strip()
    f.close()
    if line.startswith("Balance:"):
        balance = line.split(":")[1].strip()
        if balance:
            float_balance = float(balance[1:])
            if float_balance >= float(withdraw_amount):
                float_balance -= float(withdraw_amount)
                f = open("bank_data.txt", "w")
                f.write(f"Balance: ${float_balance:.2f}")
                print(f"You have withdrawn ${float(withdraw_amount):.2f}")
                print(f"Your new balance is ${float_balance:.2f}")
            else:
                print("Error: Insufficient funds.")
        else:
            print("Error: The balance value is empty.")
    else:
        print("Error: The line does not start with 'Balance:'")

def deposit():
    show_balance = open("bank_data.txt", "r")
    line = show_balance.readline().strip()
    print(f"Your current balance is ${line.split(': $')[1]}")
    show_balance.close()
    deposit_amount = input("Enter the amount you want to deposit: $")
    f = open("bank_data.txt", "r")
    line = f.readline().strip()
    f.close()
    if line.startswith("Balance:"):
        balance = line.split(":")[1].strip()
        if balance:
            float_balance = float(balance[1:])
            float_balance += float(deposit_amount)
            f = open("bank_data.txt", "w")
            f.write(f"Balance: ${float_balance:.2f}")
            print(f"You have deposited ${float(deposit_amount):.2f}")
            print(f"Your new balance is ${float_balance:.2f}")
        else:
            print("Error: The balance value is empty.")
    else:
        print("Error: The line does not start with 'Balance:'")

def main():
    print("Welcome to Bank Program!")
    while True:
        user_input = input("1. Check your Balance (1)\n2. Withdraw from your Bank (2)\n3. Deposit to your Bank (3)\n4. Quit (4)\nYour Choice: ")
        
        if user_input == "1":
            balance()
        
        elif user_input == "2":
            withdraw()
            
        elif user_input == "3":
            deposit()
            
        elif user_input == "4":
            print("Thank you for using Bank!\nHave a great day!")
            break
        
        else:
            print("Invalid Choice. Please try again.")
    
main()