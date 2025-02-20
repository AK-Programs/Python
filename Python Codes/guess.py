# Advanced Code-1
# Guess Number
num = int(input("Guess any number: "))

# Computer Guess
computer_guess = (num * 3 + 7) % 100  

# Check if User's Guess is Bigger or Small
if computer_guess < num:
    print("You won! Your guess is higher.","Computer guess:",computer_guess)
elif computer_guess > num:
    print("You lost! The computer's guess is higher.","Computer guess:",computer_guess)
else:
    print("Computer's guess and your guess are the same! Computer:",computer_guess,"You:",num)