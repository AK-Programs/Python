# Calendar View

# This script allows the user to view a calendar for a specific year.
# The user can choose to view the entire year or a specific month.
# The script will prompt the user to enter a valid year (between 1 and 9999).
# If the user chooses to view a specific month, they will be prompted to enter a valid month (between 1 and 12).
# After displaying the calendar, the user will be asked if they want to view another calendar.
# The script will continue to run until the user chooses to exit.

import calendar

def calendar_view():
    while True:
        year = int(input("Enter the year: "))
        if year >= 1 and year <= 9999:
            break
        else:
            print("Invalid year. Please try again.")
            continue

    include_month = input(f"Would you like to view the specific month in {year}? (y/n): ").lower()

    if include_month == "y":
        while True:
            month = int(input("Enter the month: "))
            if month >= 1 and month <= 12:
                break
            else:
                print("Invalid month. Please try again.")
                continue
        print(calendar.month(year, month))

    elif include_month == "n":
        print(calendar.calendar(year))
    
    else:
        print("Invalid input. Please try again.")
        return
    
    next_year = input("Would you like to view another calendar? (y/n): ").lower()
    
    if next_year == "y":
        return True
    elif next_year == "n":
        print("Goodbye!")
        return False
    else:
        print("Invalid input. Please try again.")
        return

while True:
    if not calendar_view():
        break
