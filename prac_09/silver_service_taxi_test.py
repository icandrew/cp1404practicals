"""
CP1404 - Programming II Practical 09
Silver Service Taxi Test
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    test_car = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)
    test_car.drive(0)
    print(test_car)


main()
