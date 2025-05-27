"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

# Define menu options for user interaction
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

# Repeat until user chooses to quit
while choice != "Q":
    if choice == "C":
        # Celsius to Fahrenheit conversion
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # Fahrenheit to Celsius conversion
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        # Handle invalid input
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")