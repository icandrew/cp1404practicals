"""
CP1404 - Programming II Practical 09
UnreliableCar Test
"""

from unreliable_car import UnreliableCar


def main():
    test_car = UnreliableCar(name="Nissan Skyline", reliability=60.50)
    test_car.drive(50)
    print(test_car)


main()
