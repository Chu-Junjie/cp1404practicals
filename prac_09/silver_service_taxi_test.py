"""Test script for the SilverServiceTaxi class."""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Create a SilverServiceTaxi, drive it for 18 km."""
    taxi = SilverServiceTaxi("Fancy Car", 100, 2)

    taxi.drive(18)
    print(taxi)
    fare = taxi.get_fare()
    print(f"Fare for 18km: $ {fare:.2f}")
    assert round(fare, 2) == 48.78

if __name__ == "__main__":
    main()