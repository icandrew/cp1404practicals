"""
CP1404 Practical 07 - Project Management
Estimated time to complete 150min
Time to complete - 3hours 42mins
"""
import datetime
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
            save_projects(projects, FILENAME)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
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


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i}. {project}")

    choice = int(input("Project Choice: "))
    while choice > len(projects) or choice < 0:
        try:
            print("Invalid Choice")
            choice = int(input("Project Choice: "))
        except ValueError:
            print("Invalid Choice")
    print(f"{projects[choice]}")
    new_percentage = input("New Percentage: ")
    new_percentage = check_new_percentage(new_percentage)
    projects[choice].completion = int(new_percentage)
    new_priority = input("New Priority: ")
    new_priority = check_new_priority(new_priority)
    projects[choice].priority = int(new_priority)
    print(f"Project {choice} updated to {projects[choice]}")


def check_new_percentage(new_percentage):
    while not new_percentage.isdigit() or int(new_percentage) < 0 or int(new_percentage) > 100:
        try:
            print("Percentage must be an integer between 0 and 100.")
            new_percentage = input("New Percentage: ")
        except ValueError:
            print("Invalid Percentage")
    return new_percentage


def check_new_priority(new_priority):
    while not new_priority.isdigit() or int(new_priority) < 0 or int(new_priority) > 10:
        try:
            print("Priority must be an integer between 0 and 10.")
            new_priority = input("New Priority: ")
        except ValueError:
            print("Invalid Percentage")
    return new_priority


def filter_projects(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))


def add_project(projects):
    print("Let's add a new project")
    project_name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    try:
        cost_estimate = float(input("Cost estimate: $"))
    except ValueError:
        print("Invalid cost estimate")
        return
    try:
        project_status = int(input("Percent complete: "))
    except ValueError:
        print("Invalid percentage")
        return

    new_project = Project(project_name, start_date, int(priority), cost_estimate, project_status)
    projects.append(new_project)
    print(f"Project {new_project} added")


def save_projects(projects, FILENAME):
    with open(FILENAME, "w", encoding="utf-8") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}"
                           f"\t{project.cost_estimate}\t{project.completion}\n")


main()
