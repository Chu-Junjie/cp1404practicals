"""
CP1404 - Programming II
taxi_simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxis}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except(ValueError, IndexError):
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi:
