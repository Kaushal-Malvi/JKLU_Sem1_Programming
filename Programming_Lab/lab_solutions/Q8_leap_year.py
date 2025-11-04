# Program 8: Check leap year with validation.
year = int(input("Enter a year: "))
if year <= 0:
    print("Invalid year")
elif (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
