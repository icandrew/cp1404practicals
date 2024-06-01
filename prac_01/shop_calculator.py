"""
Shop Calculator
"""

number_of_items = int(input("Number of items: "))
total_price = 0.0  # Initialize total price as a float
DISCOUNT = 0.10
DISCOUNT_THRESHOLD = 100

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for item in range(0, number_of_items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > DISCOUNT_THRESHOLD:
    total_price *= (1 - DISCOUNT)
    print(f"Total price for {number_of_items} items is ${total_price:.2f} <- 10% discount is applied")
else:
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")
