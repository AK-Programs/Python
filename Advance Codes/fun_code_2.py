# Fun Code-1
print("Can you guess the number of unique alphabets from the given list?")
values = print("A, A, B, C, D, E, E, F, G, G, G, J, Y, O")
count = {
    "A", "A", "B", "C", "D", "E", "E", "F", "G", "G", "G", "J", "Y", "O"
}

# Ask the user to guess the number of unique alphabets
guess = int(input("Enter how many unique alphabets are written above: "))

# Check if the user's guess is correct or incorrect
if guess == len(count):
    print("You are correct!")
else:
    print(f"You are INCORRECT! The correct number is {len(count)}.")
