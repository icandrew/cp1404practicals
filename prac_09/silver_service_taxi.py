"""
CP1404 - Programming II Practical 09
Silver Service Taxi Class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Initialize SilverServiceTaxi, that inherits from Taxi."""

    def __init__(self, fanciness=float, **kwargs):
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
