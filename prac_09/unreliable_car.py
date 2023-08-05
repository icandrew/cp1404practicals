"""
CP1404 - Programming II Practical 09
UnreliableCar class
"""
from car import Car
import random


class UnreliableCar(Car):
    """Initialize UnreliableCar, based on parent class Car."""

    def __init__(self, reliability=float, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability value"""
        return f"{super().__str__()}, {self.reliability} reliable"

    def drive(self, distance):
        """Generate random number and only drive the car if that number is less than the car's reliability."""
        random_number = random.randint(0, 100)
        if random_number <= self.reliability:
            print(f"The car is driving {distance} km.")
            print(f"Random Number is {random_number}")
            return distance
        else:
            print(f"The car is unreliable and won't drive {distance} km.")
            print(f"Random Number is {random_number}")
            return 0
