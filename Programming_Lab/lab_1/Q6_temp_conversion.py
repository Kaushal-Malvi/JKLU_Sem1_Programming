# Program 6 — Celsius to Fahrenheit and Kelvin

# ---- Code ----
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)

# ---- Explanation (line by line) ----
# 1) celsius = float(input("Enter temperature in Celsius: "))
#    - Reads the Celsius value as a decimal number.
# 2) fahrenheit = (celsius * 9/5) + 32
#    - Conversion formula from °C to °F.
# 3) kelvin = celsius + 273.15
#    - Conversion formula from °C to K.
# 4) print("Fahrenheit:", fahrenheit)
#    - Shows the value in °F.
# 5) print("Kelvin:", kelvin)
#    - Shows the value in K.
