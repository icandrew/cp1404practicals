"""
CP1404 - Programming II Practical 09
Silver Service Taxi Class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Initialize SilverServiceTaxi, that inherits from Taxi."""
    flagfall = 4.50

    def __init__(self, name="", fuel=0, fanciness=float):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"
