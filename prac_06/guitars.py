"""
guitars
Estimate: 30 minutes
Actual:    minutes
"""
from prac_06.guitar import Guitar
guitars = []

print("My guitars!")
guitar_name = input("Name: ").title()
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(guitar)
    print(f"{guitar} added.\n")
    guitar_name = input("Name: ").title()