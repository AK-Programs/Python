# Digital Clock

# This is script displays the current time in a simple GUI.
# 'tkinter' library is used in this program for GUI and 'time' library is used for displaying the current time.
# Run this code and a GUI will appear and the time will be displayed in this GUI.

import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x300")
root.resizable(True, True)

def update_time():
    current = time.strftime("%H:%M:%S")
    time_label.config(text=current)
    root.after(1000, update_time)
    
time_label = tk.Label(root, text="hello", font=("Arial", 80, "bold"), bg="black", fg="blue")
time_label.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)
update_time()
root.mainloop()