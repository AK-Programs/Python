def odd_even():
    num = int(input("Enter a number: "))
    if(num % 2 == 0):
        print(num,"is Even")
    
    else:
        print(num,"is Odd")

    return num

odd_even()