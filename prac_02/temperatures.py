"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

# Constants
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Main program function."""
    display_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            convert_c_to_f()
        elif choice == "F":
            convert_f_to_c()
        else:
            print("Invalid option")

        display_menu()
        choice = input(">>> ").upper()

    print("Thank you.")


def display_menu():
    """Display the menu options."""
    print(MENU)


def convert_c_to_f():
    """Convert Celsius to Fahrenheit and display the result."""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def convert_f_to_c():
    """Convert Fahrenheit to Celsius and display the result."""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


main()