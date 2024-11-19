def leap_year_checker():
    while True:
        year = input("Enter a year to check it is Leap year or not: ")

        if(len(year) != 4 ):
            print("The year length should be 4 digits!")
            continue
        
        year = int(year)

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(year, "is a Leap Year")
                else:
                    print(year, "is not a Leap Year")
            else:
                print(year, "is a Leap Year")
        else:
            print(year, "is not a Leap Year")

        repeat = input("Do you want to check another year? (Y/N): ")
        if repeat != 'y' and repeat != 'Y':
            print("Exiting the Leap Year checker.")
            break
        
leap_year_checker()