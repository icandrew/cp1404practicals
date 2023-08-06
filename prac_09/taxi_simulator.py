"""
CP1404 - Programming II Practical 09
Taxi Simulator
"""
from taxi import Taxi
from car import Car
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print("Let's drive")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            pass


main()
