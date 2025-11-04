# Program 5 — Area of a circle (radius must be between 1 and 100)
# π ≈ 3.14159

# ---- Code ----
r = float(input("Enter radius (1 to 100): "))

if r >= 1 and r <= 100:
    area = 3.14159 * r * r
    print("Area of circle =", area)
else:
    print("Invalid input! Radius must be between 1 and 100.")

# ---- Explanation (line by line) ----
# 1) r = float(input("Enter radius (1 to 100): "))
#    - Reads the radius as a decimal number.
# 2) if r >= 1 and r <= 100:
#    - The lab requires the radius to be within 1..100 (inclusive).
# 3)     area = 3.14159 * r * r
#    - Formula: area = π × r × r. We use 3.14159 for π.
# 4)     print("Area of circle =", area)
#    - Shows the area.
# 5) else:
#    - Runs when the radius is outside the allowed range.
# 6)     print("Invalid input! Radius must be between 1 and 100.")
#    - Clear reason for rejection.
