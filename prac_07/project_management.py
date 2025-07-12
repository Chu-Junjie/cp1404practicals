"""
Project Management Program
Estimated time: 2 hours
"""

import datetime
from project import Project

FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = ""
    while choice != "q":
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save = input(f"Would you like to save to {FILENAME}? ").lower()
            if save in ["y", "yes"]:
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid option")

def load_projects(filename):
    projects = []
    try:
        with open(filename, "r") as file:
            file.readline()  # Skip header
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    name, start_date_str, priority, cost_estimate, completion = parts
                    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
                    project = Project(name, start_date, int(priority), float(cost_estimate), int(completion))
                    projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return projects

def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(project.to_save_format() + "\n")


def display_projects(projects):
    print("Incomplete projects: ")
    for p in sorted([p for p in projects if not p.is_complete()], key=lambda x: x.priority):
        print(f"  {p}")
    print("Completed projects: ")
    for p in sorted([p for p in projects if p.is_complete()], key=lambda x: x.priority):
        print(f"  {p}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered = [p for p in projects if p.start_date > filter_date]
        for p in sorted(filtered, key=lambda x: x.start_date):
            print(p)
    except ValueError:
        print("Invalid date format.")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)
        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")
        if new_completion:
            project.completion = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
    except (IndexError, ValueError):
        print("Invalid input.")


main()