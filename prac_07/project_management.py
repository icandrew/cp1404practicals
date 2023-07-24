"""
CP1404 Practical 07 - Project Management
Estimated time to complete 150min
Time to complete -
"""
from datetime import datetime
from project import Project

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
            load_projects(FILENAME)
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


def load_projects(FILENAME):
    projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


main()
