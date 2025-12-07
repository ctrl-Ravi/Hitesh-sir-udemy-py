"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""


from beeply.notes import *
import time
beep=beeps()

while True:
    try:
        seconds = int(input("Enter time in second:  "))
        if seconds<1:
            print("Please enter a number greater than 0")
            continue # ask again and again if number not greater than Zero
        break #its break the loop to continue to next process
    except ValueError:
        print("Invalid input, please enter a whole number")

print("\n 🔔 Timer Started.....")
for remaining in range(seconds,0, -1):
    mins, secs= divmod(remaining,60)
    time_format= f"{mins:02}:{secs:02}"
    print(f"⌚ Time Left: {time_format}", end="\r")
    time.sleep(1)

print("\n Time's up! Take a break or move on to next task.")
beep.hear('B_',1000)