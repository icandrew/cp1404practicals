"""
CP1404 - Programming II Practical 09
Band Class
"""


class Band:
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        pass

    def __str__(self):
        return f"Band: {self.name}"
