# Advanced Code-3
# Take out your grade by your percentages (Advanced) Code-2

percentage = float(input("Enter your percentages to check your Grade: "))

round_percentage = round(percentage, 2)

if(round_percentage >= 95 and round_percentage <= 100):
    print("You are Pass and you got grade A+", round_percentage,"%")

elif(round_percentage >= 100):
    print("Maximum Percentage Limit is 100!")

elif(round_percentage == 100):
    print("You are Pass and you got grade A++", round_percentage,"%")

elif(round_percentage >= 90 and round_percentage <= 95 ):
    print("You are Pass and you got grade A", round_percentage,"%")

elif(round_percentage >= 80 and round_percentage <= 90 ):
    print("You are Pass and you got grade B", round_percentage,"%")

elif(round_percentage >= 70 and round_percentage <= 80 ):
    print("You are Pass and you got grade C", round_percentage,"%")

elif(round_percentage >= 60 and round_percentage <= 70 ):
    print("You are Pass and you got grade D", round_percentage,"%")

elif(round_percentage >= 50 and round_percentage <= 60 ):
    print("You are Pass and you got grade E+", round_percentage,"%")

elif(round_percentage >= 45 and round_percentage <= 50 ):
    print("You are Pass and you got grade E", round_percentage,"%") 

else:
    print("You are Fail! and you got grade F", round_percentage,"%") 

