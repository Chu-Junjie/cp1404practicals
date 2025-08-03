"""Band class for CP1404"""

class Band:
    """Band class to store and manage multiple musicians."""

    def __init__(self, name):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.members = []

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def __str__(self):
        """Return a string showing all members of the band."""
        return "\n".join(str(member) for member in self.members)

    def play(self):
        """Return a string showing each musician playing their first instrument (or a warning)."""
        return "\n".join(member.play() for member in self.members)