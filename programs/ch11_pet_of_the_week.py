# programs/ch11_pet_of_the_week.py
"""Pick the Sunny Paws "pet of the week" for the website and the door."""
import random
from datetime import date

from ch11_animals import ANIMALS


def pet_of_the_week(animals, day):
    """Pick one animal at random. The pick stays the same all week."""
    week = day.isocalendar().week
    random.seed(day.year * 100 + week)
    return random.choice(animals)


def main():
    today = date(2026, 6, 30)  # use date.today() for the real date
    pet = pet_of_the_week(ANIMALS, today)
    print("Week of", today.strftime("%B %d, %Y"))
    print(f"Pet of the week: {pet['name']} the {pet['species'].lower()}!")
    print(f"{pet['name']} has been waiting since {pet['arrived']}.")


if __name__ == "__main__":
    main()
