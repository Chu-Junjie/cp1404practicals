"""
CP1404/CP5632 - Practical
Program to determine score status with constants
"""

MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

score = float(input("Enter score: "))

# Check and display result
if score < MIN_SCORE or score > MAX_SCORE:
    print("Invalid score")
elif score >= EXCELLENT_THRESHOLD:
    print("Excellent")
elif score >= PASS_THRESHOLD:
    print("Passable")
else:
    print("Bad")
