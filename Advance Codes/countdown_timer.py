# Countdown Timer

# This script is a simple countdown timer.
# Usage:
# 1. Run the script.
# 2. Enter the countdown time in seconds when prompted.
# 3. The timer will display the remaining time in HH:MM:SS format.
# 4. When the countdown reaches zero, it will print "Time's up!".

import time  

def countdown_timer():  
    countdown_time = int(input("Enter the time in seconds: "))   
    for x in range(countdown_time, 0, -1):  
        
        hours = x // 3600  
        minutes = (x % 3600) // 60  
        seconds = x % 60  
         
        print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end='')  
        time.sleep(1)   

    print("\rTime's up!")   

countdown_timer()