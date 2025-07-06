"""
guitars
Estimate: 30 minutes
Actual:  18  minutes
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

name_width = max(len(guitar.name) for guitar in guitars)

print()
print("... snip ...\n")
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage_string}"