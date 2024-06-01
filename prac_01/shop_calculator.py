"""
Shop Calculator
"""

item_count = int(input("Number of items: "))
total_price = 0.0  # Initialize total price as a float
DISCOUNT = 0.10

while item_count < 0:
    print("Invalid number of items!")
    item_count = int(input("Number of items: "))
for item in range(item_count):
    price = float(input(f"Price of item {item + 1}: "))
    total_price += price
if total_price > 100:
    discount_amount = total_price * DISCOUNT
    discount_price = total_price - discount_amount
    print(f"Total price for {item_count} items is ${discount_price:.2f}")
else:
    print(f"Total price for {item_count} items is ${total_price:.2f}")




