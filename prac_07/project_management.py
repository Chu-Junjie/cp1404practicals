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
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                name, start_date_str, priority, cost_estimate, completion = parts
                start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
                project = Project(name, start_date, int(priority), float(cost_estimate), int(completion))
                projects.append(project)
    return projects


main()