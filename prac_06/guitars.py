from prac_06.guitar import Guitar


def main():
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitar_to_add = Guitar(name, year, cost)
    #     guitars.append(guitar_to_add)
    #     print(f"{name} ({year}) : ${cost:.2f} added.")
    #     name = input("Name: ")

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, start=1):
            max_characters = max(len(guitar.name) for guitar in guitars)
            print(f"Guitar {i}: {guitar.name:{max_characters}} ({guitar.year}), worth $ {guitar.cost:.2f}")




main()
