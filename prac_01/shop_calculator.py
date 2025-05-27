"""
CP1404/CP5632 - Practical
Shop Calculator
"""
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.10

number_of_items = int(input("Number of items: "))

# Validate the number of items
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Initialize total price
total_price = 0

# Loop to get the price of each item and accumulate the total
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply discount if total exceeds the threshold
if total_price > DISCOUNT_THRESHOLD:
    total_price *= (1 - DISCOUNT_RATE)

print(f"Total price for {number_of_items} items is ${total_price:.2f}")