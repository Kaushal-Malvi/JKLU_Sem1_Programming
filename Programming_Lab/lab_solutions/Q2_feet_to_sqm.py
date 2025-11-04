# Program 2: Take input in feet and calculate the area in square metres.
length_ft = float(input("Enter length in feet: "))
width_ft = float(input("Enter width in feet: "))
SQFT_TO_SQM = 0.092903
area_sqm = (length_ft * width_ft) * SQFT_TO_SQM
print("Area in square metres:", area_sqm)
