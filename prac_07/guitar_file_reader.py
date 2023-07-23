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


main()
