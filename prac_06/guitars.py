from prac_06.guitar import Guitar


def main():
    name = input("Name: ")
    guitars = []
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Name: ")


main()
