# Screenshot Taker

# This code captures screenshot of the user's screen or display.
# If the user press any key except, screenshot process will begin automatically in 3 seconds.
# If the user press f then he will be exit from the code.
# After capturing screenshot, it saves in the time format. Ex: screenshot_145530406.png
# 'time',from PIL 'ImageGrab' modules are used in this code.
# If there is a problem in this code then react --> (⚒️).
# React --> (🤖) for more codes!

import time
from PIL import ImageGrab

def capture_screenshot():
    take = input("Press and enter any key to take screenshot and F to exit: ").lower()
    if take != "f":
        countdown_time = 5
        print("Prepare your screen")
        time.sleep(1)
        for x in range(countdown_time, 0, -1):  
            seconds = x % 60
            print(f"\rTaking screenshot in {seconds:02} seconds.", end='')
            time.sleep(1)
        screenshot = ImageGrab.grab()
        print("\rScreenshot captured. Just a moment...")
        time.sleep(1)
        print("Saving screenshot...")
        time.sleep(2)
        file_name = f"screenshot_{int(time.time())}.png"
        screenshot.save(file_name)
        print(f"Screenshot saved as {file_name}")
    else:
        print("GoodBye!")

capture_screenshot()