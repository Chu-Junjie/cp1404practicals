"""
guitar_test
Estimate: 20 minutes
Actual:  15  minutes
"""
from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar1.get_age())  # Expected 103. Got 103
print(guitar1.is_vintage())  # Expected True. Got True
print(guitar1)

guitar2 = Guitar("Another Guitar", 2013, 0)
print(guitar2.get_age())  # Expected 12. Got 12
print(guitar2.is_vintage())  # Expected False. Got False
