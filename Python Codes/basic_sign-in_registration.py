email = input("Enter your email address: ")
password = input("Create a passowrd: ")

while len(password) < 6:
    print("Password too short!")
    password = input("Enter a password: ")
print("Password accepted.")

confirm_password = input("Confirm your password: ")

while confirm_password != password:
    print("Password inccorrect! Try Again!")
    confirm_password = input("Confirm password Again: ")
    
while confirm_password == password:
    print("Thanks for Registration!")
    break

sign_out = str(input("Do you want to Sign Out (Yes = 'Y' No = 'N') : "))

if(sign_out == "Y" and sign_out == "y"):
    print("Signing out...")
    print("Signed out Succesfully!")
    
elif(sign_out == "N" and sign_out == "n"):
    print("Thanks for staying Signed in!")