# Program 4 — Even or Odd

# ---- Code ----
n = int(input("Enter an integer: "))

if n % 2 == 0:
    print(n, "is an even number.")
else:
    print(n, "is an odd number.")

# ---- Explanation (line by line) ----
# 1) n = int(input("Enter an integer: "))
#    - Reads a whole number from the user.
# 2) if n % 2 == 0:
#    - The % operator gives the remainder after division by 2.
#    - If remainder is 0, the number is even.
# 3)     print(n, "is an even number.")
#    - Prints the result for even numbers.
# 4) else:
#    - If remainder is not 0, it's odd.
# 5)     print(n, "is an odd number.")
#    - Prints the result for odd numbers.
