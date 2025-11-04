# Program 2 — Area from feet to square metres (1 sq.ft = 0.092903 sq.m)

# ---- Code ----
length_ft = float(input("Enter length in feet: "))
width_ft = float(input("Enter width in feet: "))

if length_ft > 0 and width_ft > 0:
    area_sqft = length_ft * width_ft
    area_sqm = area_sqft * 0.092903
    print("Area =", area_sqm, "square metres")
else:
    print("Invalid input! Length and width must be positive.")

# ---- Explanation (line by line) ----
# 1) length_ft = float(input("Enter length in feet: "))
#    - Read the length as a decimal number in FEET.
# 2) width_ft = float(input("Enter width in feet: "))
#    - Read the width as a decimal number in FEET.
# 3) if length_ft > 0 and width_ft > 0:
#    - Both measurements must be positive in real life.
# 4)     area_sqft = length_ft * width_ft
#    - Area in square feet.
# 5)     area_sqm = area_sqft * 0.092903
#    - Convert square feet to square metres using the constant.
# 6)     print("Area =", area_sqm, "square metres")
#    - Print the converted area with unit.
# 7) else:
#    - Handles zero or negative inputs.
# 8)     print("Invalid input! Length and width must be positive.")
#    - Clear message about the rule.
