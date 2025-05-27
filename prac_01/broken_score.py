"""
CP1404/CP5632 - Practical
Program to determine score status with constants
"""
MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
message = ""

score = float(input("Enter score: "))

# Check and display result
if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
else:
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Passable"
    else:
        message = "Bad"