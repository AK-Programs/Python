def factorial():
    num = int(input("Enter a number to calculate its factorial: "))
    fact = 1 
    original_num = num  


    while num > 1:
        fact *= num  
        num -= 1 

    print("Factorial of", original_num, "is:", fact)

factorial()
