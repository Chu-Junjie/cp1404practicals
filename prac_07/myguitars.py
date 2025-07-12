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


def load_guitar(filename):
    guitars = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

if __name__ == "__main__":
    main()