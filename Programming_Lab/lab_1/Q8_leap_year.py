# Program 8 — Check whether a year is a leap year (with basic validity)

# ---- Code ----
year = int(input("Enter a positive year: "))

if year > 0:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
else:
    print("Invalid input! Year must be a positive integer.")

# ---- Explanation (line by line) ----
# 1) year = int(input("Enter a positive year: "))
#    - Reads the year as a whole number.
# 2) if year > 0:
#    - Only positive years are considered valid in this simple check.
# 3)     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#    - Leap year rules:
#      * divisible by 400 -> leap
#      * else divisible by 4 but not by 100 -> leap
# 4)         print(year, "is a leap year.")
#    - Prints the leap year message.
# 5)     else:
#    - If rules do not match, it's not a leap year.
# 6)         print(year, "is not a leap year.")
#    - Prints the non-leap message.
# 7) else:
#    - Handles non-positive input like 0 or negative.
# 8)     print("Invalid input! Year must be a positive integer.")
#    - Clear reason for rejection.
