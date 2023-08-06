"""
CP1404 - Programming II Practical 09
Band Class
"""


class Band:
    def __init__(self, name=""):
        """Initialize Band, with list of musicians"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Adds musician to a band"""
        self.musicians.append(musician)

    def play(self):
        """Return a string that identify musicians with/without instrument in the band"""
        active_musician = ""
        for musician in self.musicians:
            if not musician.instruments:
                active_musician += f"{musician.name} needs an instrument!\n"
            else:
                active_musician += f"{musician.name} is playing {musician.instruments[0]}\n"
        return active_musician

    def __str__(self):
        """Return a string represenation of the Band and its members"""
        musicians_str = ", ".join([str(musician) for musician in self.musicians])
        return f"{self.name} ({musicians_str})"
