# Program 9: RD interest calculator at 7.1% p.a.
amount = float(input("Enter monthly installment amount (min 500): "))
months = int(input("Enter duration in months (min 6): "))
if amount < 500 or months < 6:
    print("Invalid input values.")
else:
    rate = 7.1 / 100
    maturity = amount * months + (amount * months * rate * (months + 1) / (12 * 2))
    print("Maturity amount will be:", maturity)
