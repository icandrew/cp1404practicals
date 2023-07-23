from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2012, 1512.9)
    print(f"{gibson.name} get_age() - Expected {101}. Got {gibson.get_age()}")
    print(f"{other.name} get_age() - Expected {11}. Got {other.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


main()
