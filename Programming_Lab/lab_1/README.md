# Lab 1 — Beginner-Style Solutions (Code + Line-by-Line Explanation)

Each file contains **simple code first**, followed by a **line-by-line explanation** inside the same `.py` file (as comments).  
No advanced patterns, no loops/try-excepts — just the minimum logic that a first-time coder can follow.

## Files (click to open)

1. [Q1_plot_area.py](Q1_plot_area.py) — Plot area in square metres  
   ```python
   length = float(input("Enter length in metres: "))
   width = float(input("Enter width in metres: "))
   if length > 0 and width > 0:
       area = length * width
       print("Area =", area, "square metres")
   else:
       print("Invalid input! Length and width must be positive.")
   ```

2. [Q2_feet_to_sqm.py](Q2_feet_to_sqm.py) — Area from feet to square metres  
   ```python
   length_ft = float(input("Enter length in feet: "))
   width_ft = float(input("Enter width in feet: "))
   if length_ft > 0 and width_ft > 0:
       area_sqft = length_ft * width_ft
       area_sqm = area_sqft * 0.092903
       print("Area =", area_sqm, "square metres")
   else:
       print("Invalid input! Length and width must be positive.")
   ```

3. [Q3_divisibility.py](Q3_divisibility.py) — Check if y is divisible by x (negative => "Invalid input")  
   ```python
   x = int(input("Enter integer x (divisor): "))
   y = int(input("Enter integer y (dividend): "))
   if x <= 0 or y < 0:
       print("Invalid input")
   else:
       if y % x == 0:
           print(y, "is divisible by", x)
       else:
           print(y, "is not divisible by", x)
   ```

4. [Q4_even_or_odd.py](Q4_even_or_odd.py) — Even/Odd checker  
   ```python
   n = int(input("Enter an integer: "))
   if n % 2 == 0:
       print(n, "is an even number.")
   else:
       print(n, "is an odd number.")
   ```

5. [Q5_area_circle.py](Q5_area_circle.py) — Circle area (radius 1–100)  
   ```python
   r = float(input("Enter radius (1 to 100): "))
   if r >= 1 and r <= 100:
       area = 3.14159 * r * r
       print("Area of circle =", area)
   else:
       print("Invalid input! Radius must be between 1 and 100.")
   ```

6. [Q6_temp_conversion.py](Q6_temp_conversion.py) — Celsius to Fahrenheit & Kelvin  
   ```python
   celsius = float(input("Enter temperature in Celsius: "))
   fahrenheit = (celsius * 9/5) + 32
   kelvin = celsius + 273.15
   print("Fahrenheit:", fahrenheit)
   print("Kelvin:", kelvin)
   ```

7. [Q7_c_f_same.py](Q7_c_f_same.py) — Where °C equals °F  
   ```python
   print("Celsius and Fahrenheit are equal at -40 degrees.")
   ```

8. [Q8_leap_year.py](Q8_leap_year.py) — Leap year with basic validity  
   ```python
   year = int(input("Enter a positive year: "))
   if year > 0:
       if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
           print(year, "is a leap year.")
       else:
           print(year, "is not a leap year.")
   else:
       print("Invalid input! Year must be a positive integer.")
   ```

9. [Q9_rd_interest.py](Q9_rd_interest.py) — RD maturity at 7.1% p.a. (simple interest)  
   ```python
   installment = float(input("Enter monthly installment (minimum Rs. 500): "))
   months = int(input("Enter duration in months (minimum 6): "))
   if installment >= 500 and months >= 6:
       rate = 7.1 / 100
       total_interest = installment * (rate / 12) * (months * (months + 1) / 2)
       maturity = installment * months + total_interest
       print("Maturity amount =", maturity)
   else:
       print("Invalid input! Minimum installment is Rs. 500 and minimum duration is 6 months.")
   ```

10. [Q10_time_from_seconds.py](Q10_time_from_seconds.py) — Seconds to H:M:S (24-hour clock)  
    ```python
    total_seconds = int(input("Enter total seconds (1 to 86400): "))
    if total_seconds >= 1 and total_seconds <= 86400:
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        print(hours, "hours,", minutes, "minutes, and", seconds, "seconds")
    else:
        print("Invalid input! Seconds must be between 1 and 86400.")
    ```
