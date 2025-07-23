"""Band class for CP1404"""

class Band:

    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician):
        self.members.append(musician)

    def __str__(self):
        return "\n".join(str(member) for member in self.members)

    def play(self):
        return "\n".join(member.play() for member in self.members)