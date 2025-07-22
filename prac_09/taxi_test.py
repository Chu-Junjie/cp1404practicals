from taxi import Taxi

def main():
    """Test the Taxi class by driving and calculating fares."""
    my_taxi = Taxi("Prius 1", 100)

    # Drive 40km
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart fare, then drive 100km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare after restart: ${my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()