"""
CP1404 Practical 07 - Project Management
Estimated time to complete 150min
Time to complete -
"""

FILENAME = "projects.txt"

MENU = """
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("Load Projects")
        elif choice == "S":
            print("Save Projects")
        elif choice == "D":
            print("Display Projects")
        elif choice == "F":
            print("Filter Projects")
        elif choice == "A":
            print("Add New Projects")
        elif choice == "U":
            print("Update Projects")
        else:
            print("Choice not valid")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


main()
