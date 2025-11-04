# Program 5: Area of Circle, radius 1 to 100 allowed.
radius = float(input("Enter radius of the circle: "))
if radius < 1 or radius > 100:
    print("Invalid radius! Must be between 1 and 100.")
else:
    area = 3.14159 * radius * radius
    print("Area of circle is", area)
