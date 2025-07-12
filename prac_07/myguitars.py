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


def load_guitar(filename):
    guitars = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
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


if __name__ == "__main__":
    main()