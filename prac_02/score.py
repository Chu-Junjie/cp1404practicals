"""
CP1404/CP5632 - Practical
Program to determine score status with constants
"""
# Constants
MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    """Main function to run the score evaluation program."""
    score = get_score()
    result = evaluate_score(score)
    print(result)


def get_score():
    """Prompt the user to enter a score and return it as a float."""
    return float(input("Enter score: "))


def evaluate_score(score):
    """Evaluate the score and return the corresponding message."""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()