import random

# constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    """Get user input and generate the requested number of quick pick lines."""
    try:
        quick_pick = int(input("How many quick picks? "))
        if quick_pick <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Generate and print the required number of quick picks
    for i in range(quick_pick):
        quick_pick = generate_quick_pick()
        quick_pick.sort()
        print("".join(f"{num:3}" for num in quick_pick))


def generate_quick_pick():
    """Generate a list of unique random numbers for one quick pick."""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER,MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    return numbers


main()