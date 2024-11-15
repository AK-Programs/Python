# Fun Code
print("Can you guess the number of unique alphabets from the given list?")
values = print("A, A, B, C, D, E, E, F, G, G, G, J, Y, O")
count = {
    "A", "A", "B", "C", "D", "E", "E", "F", "G", "G", "G", "J", "Y", "O"
}

guess = int(input("Enter how many unique alphabets are written above: "))

if guess == len(count): 
    print("You are correct!")
else:
    print(f"You are INCORRECT! The correct number is {len(count)}.")

