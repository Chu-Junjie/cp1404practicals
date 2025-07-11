"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """load data and display it."""
    data = load_data()
    display_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        subjects.append(parts)
        parts[2] = int(parts[2])
        print(parts)
        print("-----------")
        print()
    input_file.close()
    return subjects


def display_subjects(data):
    """Display subject details from data list"""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()