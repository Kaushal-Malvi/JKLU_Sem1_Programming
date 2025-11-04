# Program 1 — Area of a rectangular plot (in square metres)

# ---- Code ----
length = float(input("Enter length in metres: "))
width = float(input("Enter width in metres: "))

if length > 0 and width > 0:
    area = length * width
    print("Area =", area, "square metres")
else:
    print("Invalid input! Length and width must be positive.")

# ---- Explanation (line by line) ----
# 1) length = float(input("Enter length in metres: "))
#    - Shows a prompt to the user and reads text.
#    - float(...) converts that text to a decimal number (length can be 12.5).
#    - The number is stored in the variable 'length'.
# 2) width = float(input("Enter width in metres: "))
#    - Same as line 1, but we store the width in 'width'.
# 3) if length > 0 and width > 0:
#    - A real plot can't have zero or negative size.
#    - We check that BOTH values are strictly greater than 0.
# 4)     area = length * width
#    - Rectangle area formula: area = length × width.
# 5)     print("Area =", area, "square metres")
#    - Prints the result along with the unit.
# 6) else:
#    - Runs when at least one value is not positive (<= 0).
# 7)     print("Invalid input! Length and width must be positive.")
#    - Tells the user why the input was rejected.
