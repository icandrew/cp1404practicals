"""
CP1404 - Programming II Practical 09
Silver Service Taxi Test
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    test_white_taxi = SilverServiceTaxi(name="White Taxi", fuel=100, fanciness=4)
    test_white_taxi.drive(0)
    print(f"{test_white_taxi}\nTotal fare: ${test_white_taxi.get_fare():.2f}")
    print("---------------------")
    test_yellow_taxi = SilverServiceTaxi(name="Yellow Taxi", fuel=100, fanciness=2)
    test_yellow_taxi.drive(18)
    #  total fare is computed as price_per_km(1.23) * drive(18) * fanciness(2) + flagfall(4.50)
    print(f"{test_yellow_taxi}\nTotal fare: ${test_yellow_taxi.get_fare():.2f}")


main()
