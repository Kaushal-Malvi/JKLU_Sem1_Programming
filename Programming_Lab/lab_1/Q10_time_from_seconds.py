# Program 10 — Convert seconds (1..86400) to hours, minutes, seconds (24-hour clock)

# ---- Code ----
total_seconds = int(input("Enter total seconds (1 to 86400): "))

if total_seconds >= 1 and total_seconds <= 86400:
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    print(hours, "hours,", minutes, "minutes, and", seconds, "seconds")
else:
    print("Invalid input! Seconds must be between 1 and 86400.")

# ---- Explanation (line by line) ----
# 1) total_seconds = int(input("Enter total seconds (1 to 86400): "))
#    - Read a whole number of seconds in one day.
# 2) if total_seconds >= 1 and total_seconds <= 86400:
#    - Valid range for one day.
# 3)     hours = total_seconds // 3600
#    - Integer division by 3600 gives total full hours.
# 4)     remaining = total_seconds % 3600
#    - The leftover seconds after removing full hours.
# 5)     minutes = remaining // 60
#    - Full minutes in the remaining seconds.
# 6)     seconds = remaining % 60
#    - Leftover seconds after minutes.
# 7)     print(hours, "hours,", minutes, "minutes, and", seconds, "seconds")
#    - Nicely formatted output.
# 8) else:
#    - Handles values outside the allowed range.
# 9)     print("Invalid input! Seconds must be between 1 and 86400.")
#    - Clear rule reminder.
