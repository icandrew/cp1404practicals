"""
CP1404 - Programming II Practical 09
Test Taxi
"""
from taxi import Taxi


def main():
    my_taxi = Taxi(name="Prius 1", fuel=100, price_per_km=1.23)
    print(f"{my_taxi}")


main()