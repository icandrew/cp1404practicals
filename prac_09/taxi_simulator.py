"""
CP1404 - Programming II Practical 09
Taxi Simulator
"""
from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    current_taxi = None
    print("Let's drive")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            current_taxi = select_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                pass
        else:
            print("Invalid option")
            break
    print(f"Total trip cost: {bill_to_date}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")



def select_taxi(taxis):
    try:
        selected_taxi = int(input("Choose Taxi:"))
        if 1 <= selected_taxi <= len(taxis):
            return taxis[selected_taxi - 1]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print(f"Choice must be a number  not more than {len(taxis)}")


main()
