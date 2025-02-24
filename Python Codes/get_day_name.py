import calendar
def get_day_name():
    
    while True:
        year = int(input("Enter the year: "))
        if year >= 1 and year <= 9999:
            break
        
        else:
            print("Invalid year. Please try again.")
            continue
    
    while True:
        month = int(input("Enter the month: "))
        if month >= 1 and month <= 12:
            break
        
        else:
            print("Invalid month. Please try again.")
            continue
    while True:
        day = int(input("Enter the day: "))
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day >= 1 and day <= 29:
                    break
                else:
                    print("Invalid day. Please try again.")
                    continue
            else:
                if day >= 1 and day <= 28:
                    break
                else:
                    print("Invalid day. Please try again.")
                    continue
        elif month in [4, 6, 9, 11]:
            if day >= 1 and day <= 30:
                break
            else:
                print("Invalid day. Please try again.")
                continue
        else:
            if day >= 1 and day <= 31:
                break
            else:
                print("Invalid day. Please try again.")
                continue

    day_name = calendar.day_name[calendar.weekday(year,month,day)]
    print(f"The day is: {day_name}")
    next_day_name = input("Would you like to get another day name? (y/n): ").lower()

    if next_day_name == "y":
        return True

    elif next_day_name == "n":
        print("Goodbye!")
        return False

    else:
        print("Invalid input. Please try again.")
        return

while True:
   if not get_day_name():
       break