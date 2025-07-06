"""
programming language
Estimate: 30 minutes
Actual:   15 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a formatted string with details about the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
