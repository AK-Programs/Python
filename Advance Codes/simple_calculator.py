def simple_calculator():
    print("Welcome to our Calculator!")

    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Choose an operator ('Addition (+)', 'Subtraction (-)', 'Multiplication (*)', 'Division (/)'): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                continue  

        else:
            print("Error: Invalid operator! Please choose '+', '-', '*', or '/'.")
            continue  

        
        int_result = int(result)
        if result == int_result:
            print("Answer =", int_result)
        else:
            decimal_points = int(input("How many decimal points should the answer have? "))
            rounded_result = round(result, decimal_points)
            print("Answer =", rounded_result)

        
        repeat = input("Would you like to perform another calculation? 'Yes (Y) or No (N)': ")
        if repeat == "y" and repeat == "Y":
            continue  
        elif repeat == "n" and repeat == "N":
            print("Goodbye!")
            break 
        else:
            print("Invalid choice! Exiting the calculator.")
            break

simple_calculator()