"""
CP1404/CP5632 Practical
State names in a dictionary
State names in a dictionary (PEP8 + improvements)

Estimated time: 15 minutes
Actual time: 12 minutes
"""

# State abbreviations mapped to full state names with PEP8 style.
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

# Print all state codes and names (aligned)
print("All state codes:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")  # Align codes to 3 characters

# Get user input and handle both upper/lowercase
state_code = input("Enter short state: ").upper()
# Use exceptions and the "Easier to Ask Forgiveness than Permission" (EAFP) approach.
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
