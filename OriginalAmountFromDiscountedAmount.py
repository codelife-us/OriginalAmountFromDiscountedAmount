# What is the original amount given a discounted percentage and known amount charged
# Show amount saved
import sys
try:
    discounted_amount = float(input("What is the discounted amount? "))
except ValueError:
    print("Invalid input. Enter a numerical amount.")
    sys.exit(1)
if discounted_amount < 0:
    print("Discounted amount must be greater than zero.")
    sys.exit(1)
try:
    percentage = float(input("What is the percentage discount (Example enter 70 for 70%)? "))
except ValueError:
    print("Invalid input. Enter a numerical amount.")
    sys.exit(1)
if percentage >= 100 or percentage < 0:
    print("Percentage must be zero or greater and less than one hundred.")
    sys.exit(1)
else:    
    original_amount = discounted_amount * (1 / (1 - percentage / 100))
    print(f"The original amount would have been ${original_amount:,.2f}.")
    savings_amount = original_amount - discounted_amount

    print(f"The savings amount is ${savings_amount:,.2f}.")
