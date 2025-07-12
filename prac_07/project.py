"""
project.py
Project class for the Project Management Program
"""

import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date  # datetime.date
        self.priority = priority      # int
        self.cost_estimate = cost_estimate  # float
        self.completion = completion  # int (percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        return self.priority < other.priority