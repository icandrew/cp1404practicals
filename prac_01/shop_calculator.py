item_count = int(input("Number of Items:"))
item_list = []


def main():
    for item in range(item_count):
        item_price = float(input("Price of item: "))
        item_list.append(item_price)
        total_price = sum(item_list)

    discount = discounted_price(total_price)
    if total_price > 100:
        print(f"Total price for {item_count} items is ${discount:.2f}")
    else:
        print(f"Total price for {item_count} items is ${total_price:.2f}")


def discounted_price(total_price):
    return total_price - (total_price * 0.10)


main()
