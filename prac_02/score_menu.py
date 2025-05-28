"""
score_menu.py
"""
from score import evaluate_score

MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
MENU = """\nMenu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Main function: control menu and logic using standard pattern."""
    score = 0

    display_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")

        display_menu()
        choice = input(">>> ").upper()

    print("Farewell!")


def get_valid_score():
    """Prompt user for a valid score (between MIN_SCORE and MAX_SCORE)."""
    score = float(input(f"Enter score ({MIN_SCORE}-{MAX_SCORE}): "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid input.")
        score = float(input(f"Enter score ({MIN_SCORE}-{MAX_SCORE}): "))
    return score


def display_menu():
    """Display the main menu."""
    print(MENU)


def print_result(score):
    """Print the evaluation result of the score."""
    print(evaluate_score(score))


def show_stars(score):
    """Print stars equal to the score value (rounded)."""
    print("*" * int(round(score)))


main()