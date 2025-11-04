# Program 3 — Check if y is divisible by x
# Note: For negative integers, we display "Invalid input" (as per lab sheet).
#       x must also not be zero (division by zero is undefined).

# ---- Code ----
x = int(input("Enter integer x (divisor): "))
y = int(input("Enter integer y (dividend): "))

if x <= 0 or y < 0:
    print("Invalid input")
else:
    if y % x == 0:
        print(y, "is divisible by", x)
    else:
        print(y, "is not divisible by", x)

# ---- Explanation (line by line) ----
# 1) x = int(input("Enter integer x (divisor): "))
#    - Reads x as a whole number (divisor).
# 2) y = int(input("Enter integer y (dividend): "))
#    - Reads y as a whole number (dividend).
# 3) if x <= 0 or y < 0:
#    - Per instructions, negative inputs are invalid.
#    - Also, x cannot be 0 because we cannot divide by 0.
# 4)     print("Invalid input")
#    - Matches the exact message required.
# 5) else:
#    - Inputs are valid, so we check divisibility.
# 6)     if y % x == 0:
#    - If remainder is 0, y is divisible by x.
# 7)         print(y, "is divisible by", x)
#    - Prints a positive message.
# 8)     else:
#    - Otherwise not divisible.
# 9)         print(y, "is not divisible by", x)
#    - Prints a negative message.
