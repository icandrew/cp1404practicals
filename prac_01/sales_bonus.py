"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
percentage = 0
while sales >= 0:
    if sales <= 999:
        percentage = 0.1
        bonus = percentage * sales
        print(f"Your bonus is ${bonus}")
        sales = float(input("Enter sales: $"))
    elif sales >= 1000:
        percentage = 0.15
        bonus = percentage * sales
        print(f"Your bonus is ${bonus}")
        sales = float(input("Enter sales: $"))
print(f"Invalid input")
