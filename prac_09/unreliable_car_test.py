from prac_09.unreliable_car import Unreliable_car

def main():
    """Test the UnreliableCar class by attempting to drive it multiple times."""

    # Create a car which have 30% reliable.
    car = Unreliable_car("Old Bomb", 100, 30)

    # Try to drive 10 times and each time drive 10km.
    for i in range(10):
        distance_driven = car.drive(10)
        print(f"Attempt {i + 1}: drove {distance_driven}km, fuel left: {car.fuel}, odometer: {car.odometer}")

if __name__ == "__main__":
    main()