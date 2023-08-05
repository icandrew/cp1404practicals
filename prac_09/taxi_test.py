"""
CP1404 - Programming II Practical 09
Test Taxi
"""
from taxi import Taxi


def main():
    my_taxi = Taxi(name="Prius 1", fuel=100)
    my_taxi.drive(40)
    print(f"{my_taxi}\nCurrent fare: ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}\nCurrent fare: ${my_taxi.get_fare():.2f}")


main()
