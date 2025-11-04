# Program 10: Convert seconds to hh:mm:ss (1 to 86400 only).
sec = int(input("Enter seconds (1 to 86400): "))
if sec < 1 or sec > 86400:
    print("Invalid input")
else:
    hours = sec // 3600
    sec = sec % 3600
    minutes = sec // 60
    seconds = sec % 60
    print(hours, "hours,", minutes, "minutes and", seconds, "seconds")
