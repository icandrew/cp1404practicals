"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


# sales = float(input("Enter sales: $"))
# threshold = 1000
# over_threshold = sales * 15 / 100
# under_threshold = sales * 10 / 100
#
# if sales >= 1000:
#     print(f"Bonus: {over_threshold}")
# else:
#     print(f"Bonus: {under_threshold}")


def sales_threshold(low, high):
    sales = float(input("Enter sales: $"))
    if sales >= high:
        print(f"Bonus: ${upper_threshold}")
    elif high > sales > low:
        under_threshold = sales * 10 / 100
        print(f"Bonus: ${under_threshold}")
    else:
        print("No Bonus")


sales_threshold(0, 1000)
