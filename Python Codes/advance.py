# This is a practice code if you want to run this So i can run

# num = int(input("Enter a number to check 2/4 of : "))

# if(num > 4 ):
#     print("2 x",num,"Ans:",2*num,"/ 4 = ",num/4)

# elif(num == 3):
#     print("2 x",num,"/4","Ans:",2*num,"/ 4 = ",num/4)

# elif(num % 2 == 0):
#     print("2 divide by 4","Ans:",num,"/ 2")

# elif(num / 2 ):
#     print(" 2 divide by ", num, "/ 4 = ", num/4, "Ans: ", num)


# Take out your Percentages in your subjects (Advanced) Code-1
print("How to take out your percentages in your subjects (Tell your score in each subject below then we will give you your percentage)")
outof = int(input("What is the Maxmimum marks of each subject: ")) 
sub1 = int(input("Enter your score in Maths: "))
sub2 = int(input("Enter your score in Grammer: "))
sub3 = int(input("Enter your score in Literature: "))
sub4 = int(input("Enter your score in Science/EVS: "))
sub5 = int(input("Enter your score in Social Science: "))

# If Hindi subject is not in your school So, Type 0 
sub6 = int(input("Enter your score in Hindi (If this subject is not in your school then Type 0) : ")) 

# If Gujarati subject is not in your school So, Type 0 
sub7 = int(input("Enter your score in Gujarati (If this subject is not in your school then Type 0) : "))

total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 
print("Total marks obtained in all subjects =", total)

maximum = outof*7
print("Maximum marks in all subjects =", maximum)

percentage = total/maximum*100
# round_percentage = round(percentage, 2) Means, it is doing rounding of the two decimal place (Hundredths)
round_percentage = round(percentage, 2)

print("You got", round_percentage,"% Percentages")


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

