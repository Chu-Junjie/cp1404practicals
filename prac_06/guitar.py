"""
guitar
Estimate: 20 minutes
Actual:    minutes
"""
class Guitar:
    """Represent a guitar with name, year, and cost."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"