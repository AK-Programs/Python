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
# Comment How many Percentage you got!
