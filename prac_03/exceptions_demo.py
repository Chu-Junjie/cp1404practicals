"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user enters something that is not an integer, e.g. "abc" or "3.5".

2. When will a ZeroDivisionError occur?
When the user enters 0 as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes. can use a while loop to check that the denominator is not zero before doing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")