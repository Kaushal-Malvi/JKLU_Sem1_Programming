# Program 9 — RD maturity at 7.1% p.a. (simple per-installment interest, no compounding)

# ---- Code ----
installment = float(input("Enter monthly installment (minimum Rs. 500): "))
months = int(input("Enter duration in months (minimum 6): "))

if installment >= 500 and months >= 6:
    rate = 7.1 / 100  # annual rate
    # Simple idea: first deposit stays for 'months' months, next stays for 'months-1', ..., last stays for 1
    total_interest = installment * (rate / 12) * (months * (months + 1) / 2)
    maturity = installment * months + total_interest
    print("Maturity amount =", maturity)
    print("Principal =", installment * months, "| Interest =", total_interest)
else:
    print("Invalid input! Minimum installment is Rs. 500 and minimum duration is 6 months.")

# ---- Explanation (line by line) ----
# 1) installment = float(input("Enter monthly installment (minimum Rs. 500): "))
#    - Monthly deposit amount.
# 2) months = int(input("Enter duration in months (minimum 6): "))
#    - Number of months for the RD.
# 3) if installment >= 500 and months >= 6:
#    - Bank rules: at least Rs. 500 per month and at least 6 months.
# 4)     rate = 7.1 / 100
#    - Convert percent to decimal (e.g., 7.1% => 0.071).
# 5)     total_interest = installment * (rate / 12) * (months * (months + 1) / 2)
#    - Each monthly deposit earns interest for a different number of months.
#    - The sum 1 + 2 + ... + months = months*(months+1)/2 counts those months of interest.
# 6)     maturity = installment * months + total_interest
#    - Total payout = principal + interest.
# 7)     print("Maturity amount =", maturity)
#    - Shows the final amount.
# 8)     print("Principal =", installment * months, "| Interest =", total_interest)
#    - Breaks out principal and interest for clarity.
# 9) else:
#    - Handles values below the required limits.
# 10)    print("Invalid input! Minimum installment is Rs. 500 and minimum duration is 6 months.")
#    - Clear rule reminder.
