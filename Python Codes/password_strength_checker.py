# If password is less than 6 characters then Password is not accepted
# If password is equal to 6 or more than 6 characters then password is accepted

password = input("Enter a password: ")

while len(password) < 6:
    print("Password too short!")
    password = input("Enter a password: ")
print("Password accepted.")