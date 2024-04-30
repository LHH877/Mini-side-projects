# Import necessary libraries
from playsound import playsound  # Library for playing sound files
import time  # Library for time-related operations

# ANSI escape codes for clearing console output
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Function to set an alarm
def alarm(seconds):
    time_elapsed = 0  # Initialize time elapsed counter to 0

    print(CLEAR)  # Clear the console output
    while time_elapsed < seconds:  # Continue loop until time elapsed equals specified seconds
        time.sleep(1)  # Pause execution for 1 second
        time_elapsed += 1  # Increment time elapsed counter by 1 second

        # Calculate time remaining in minutes and seconds
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # Print the time remaining in minutes and seconds
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    # Play the alarm sound once time elapsed equals specified seconds
    playsound("alarm_clock_sound.mp3")

# Get input from the user for minutes and seconds
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))

# Calculate total seconds to wait
total_seconds = minutes * 60 + seconds

# Call the alarm function with total seconds
alarm(total_seconds)
