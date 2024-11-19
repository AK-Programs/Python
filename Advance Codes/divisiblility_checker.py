def divisibility_checker():
    while True:
        dividend = float(input("Enter the Dividend: "))
        divisor = float(input("Enter the Divisor: "))

        if(dividend % divisor == 0):
            print(dividend,"is divisible by",divisor)

        else:
            print(dividend,"is not divisible by",divisor)
    
divisibility_checker()
