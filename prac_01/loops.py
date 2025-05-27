# a. count in 10s from 0 to 100:
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1:
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
number_of_stars = int(input("number of stars: "))

i = 0
while i < number_of_stars:
    print("*", end="")
    i += 1

print()

# d. print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1 with no blank line.
# E.g., if the user entered 4, your single loop should print:
number_of_lines = int(input("number of lines: "))

i = 1
while i <= number_of_lines:
    print("*" * i)
    i += 1

print()