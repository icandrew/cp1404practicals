"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
UPPER_THRESHOLD = 0.15
LOWER_THRESHOLD = 0.10
CEILING_SALES = 1000
while sales >= 0:
    if sales >= CEILING_SALES:
        bonus = sales * UPPER_THRESHOLD
    else:
        bonus = sales * LOWER_THRESHOLD

    print(f"Your bonus is ${bonus}")
    sales = float(input("Enter sales: $"))
print(f"Invalid input")
