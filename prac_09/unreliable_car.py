"""
CP1404/CP5632 Practical
Car class
"""

from prac_09.car import Car

class unreliable_car(Car):
    """An unreliable car that sometimes doesn't drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

