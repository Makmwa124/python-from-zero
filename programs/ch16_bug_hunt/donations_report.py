# programs/ch16_bug_hunt/donations_report.py
"""Sunny Paws donations report (as Rosa found it, bugs and all).

Run from the programs/ch16_bug_hunt folder:  python3 donations_report.py
"""
import csv

DONATIONS_FILE = "../../data/donations.csv"


def load_donations(path):
    """Read the donations CSV into a list of dicts (amounts as ints)."""
    donations = []
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            row["amount"] = int(row["amount"])
            donations.append(row)
    return donations


def total(donations):
    """Add up every donation."""
    result = 0
    for gift in donations:
        result += gift["amount"]
    return result


def total_by_month(donations):
    """Return a dict like {"2026-01": 1234, ...}."""
    totals = {}
    for gift in donations:
        month = gift["date"][:7]
        totals[month] = gift["amount"]
    return totals


def average_gift(donations):
    """Return the average donation in dollars."""
    return total(donations) / len(donations)


def print_report(donations):
    print("Sunny Paws donations report")
    print("=" * 27)
    for month, amount in total_by_month(donations).items():
        print(f"{month}  ${amount:>6,}")
    print(f"Total    ${total(donations):>6,}")
    print(f"Average gift: ${average_gift(donations):.2f}")


if __name__ == "__main__":
    print_report(load_donations(DONATIONS_FILE))
