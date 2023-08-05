"""
CP1404 - Programming II Practical 09
UnreliableCar class
"""
from car import Car


class UnreliableCar(Car):
    """Initialize UnreliableCar, based on parent class Car."""
    def __init__(self, reliability=float, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, {self.reliability} reliable"


