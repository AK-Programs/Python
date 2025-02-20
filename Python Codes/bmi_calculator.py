def bmi_calculator():
    print("Welcome to BMI Calculator")

    while True:

        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        bmi = weight / (height ** 2)
        round_bmi = round(bmi, 2)
        print("Your BMI is",round_bmi)

        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")

        repeat = input("Would you like to perform another BMI calculation? 'Yes (Y) or No (N)': ")
        if repeat == "y" and repeat == "Y":
            continue  
        elif repeat == "n" and repeat == "N":
            print("Goodbye!")
            break 
        else:
            print("Invalid choice! Exiting the BMI calculator.")
            break

bmi_calculator()