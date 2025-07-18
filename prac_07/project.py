"""
project.py
Project class for the Project Management Program
"""

import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion >= 100

    def to_save_format(self):
        return (f"{self.name}\t{self.start_date}\t{self.priority}"
                f"\t{self.cost_estimate}\t{self.completion}")