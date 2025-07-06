"""
Wimbledon Champions Program
Estimated time: 25 minutes
Actual time: 22 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data and display champions with their win counts and countries."""
    data = read_csv_data(FILENAME)
    champion_wins = count_champion_wins(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def read_csv_data(filename):
    """Read Wimbledon data from CSV and return a list of rows (excluding header)."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]  # Skip header
    return [line.strip().split(",") for line in lines]


def count_champion_wins(data):
    """Return a dictionary of champions and how many times they have won."""
    champion_to_wins = {}
    for row in data:
        champion = row[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_countries(data):
    """Return a sorted set of countries that have produced Wimbledon champions."""
    countries = {row[1] for row in data}
    return sorted(countries)


main()
