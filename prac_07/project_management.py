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
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects(FILENAME)
        elif choice == "S":
            print("Save Projects")
        elif choice == "D":
            display_projects(projects)
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


def display_projects(projects):
    if len(projects) > 0:
        print("Incomplete Projects:")
        for project in projects:
            if not project.is_completed():
                print(f"{project}")
        print("Completed Projects:")
        for project in projects:
            if project.is_completed():
                print(f"{project}")
    else:
        print("No projects available.")


main()



main()

