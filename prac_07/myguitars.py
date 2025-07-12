"""
my guitars.py
"""

import csv

from prac_07.guitar import Guitar

def main():
    filename = 'guitars.csv'
    guitars = load_guitar(filename)
    print("All guitars:")
    for guitar in guitars:
        print(guitar)

    add_new_guitars(guitars)
    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)

    write_guitars_to_file(filename, guitars)


def load_guitar(filename):
    """Load guitars from CSV file with proper header handling"""
    guitars = []
    try:
        with open(filename, 'r') as file:
            file.readline()
            csv_reader = csv.reader(file)
            for row in csv_reader:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list.")
    return guitars


def add_new_guitars(guitars):
    print("\nAdd new guitars (leave name blank to finish):")
    name = input("Name: ")
    while name:
        try:
            year = int(input("Enter year: "))
            cost = float(input("Enter cost: "))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"Added: {new_guitar}")
        except ValueError:
            print("Invalid input. Please enter a valid year and cost.")
        name = input("Name: ")


def write_guitars_to_file(filename, guitars):
    """Write the guitars to a CSV file (overwrite existing)."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Year", "Cost"])
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()