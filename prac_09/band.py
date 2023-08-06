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
        active_musician = ""
        for musician in self.musicians:
            if not musician.instruments:
                active_musician += f"{musician.name} needs an instrument!\n"
            else:
                active_musician += f"{musician.name} is playing {musician.instruments[0]}\n"
        return active_musician
        

    def __str__(self):
        return f"Band: {self.name}"
