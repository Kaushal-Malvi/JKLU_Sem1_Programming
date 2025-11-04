# Program 3: Check if y is divisible by x.
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
if x < 0 or y < 0:
    print("Invalid input")
elif y % x == 0:
    print(y, "is divisible by", x)
else:
    print(y, "is not divisible by", x)
