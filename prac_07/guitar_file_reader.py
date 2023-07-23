"""
Complete first part of More Guitars exercise
"""

from guitar import Guitar


def main():
    guitars = []
    with open("guitars.csv", "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)
        guitars.sort()
        for guitar in guitars:
            print(guitar)

    print(f"\n-- Enter your new guitar --")
    name = input("Guitar name: ")
    while name != "":
        add_new_guitar(guitars, name)
        add_guitar = input("Add more? (y/n) ").upper()
        if add_guitar != "Y":
            break
        name = input("Guitar name: ")
        if not name:
            break
    print("Thank you!")
    update_guitar_file(guitars)


def update_guitar_file(guitars):
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(guitar.name, guitar.year, guitar.cost, sep=',', file=out_file)
    out_file.close()


def add_new_guitar(guitars, name):
    year = int(input("Year: "))
    cost = float(input("Cost: $ "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} has been added.")


main()
