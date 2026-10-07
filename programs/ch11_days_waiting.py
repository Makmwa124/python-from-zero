# programs/ch11_days_waiting.py
"""How long has each available animal been waiting for a home?"""
from datetime import date

from ch11_animals import ANIMALS


def days_since(date_text, today):
    """Return the number of days from a "YYYY-MM-DD" date to today."""
    arrived = date.fromisoformat(date_text)
    return (today - arrived).days


def main():
    today = date(2026, 6, 30)  # use date.today() for the real date
    print("Days at Sunny Paws, as of", today.strftime("%A, %B %d, %Y"))
    print("-" * 44)
    for animal in ANIMALS:
        days = days_since(animal["arrived"], today)
        weeks = days // 7
        print(f"{animal['name']:<8} {days:>4} days  (about {weeks} weeks)")
    waits = [days_since(a["arrived"], today) for a in ANIMALS]
    print("-" * 44)
    print(f"Longest wait: {max(waits)} days. Shortest: {min(waits)} days.")


if __name__ == "__main__":
    main()
