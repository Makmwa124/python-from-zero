# programs/ch10_age_converter.py
"""Convert a pet's age to human years, using the shelter's poster."""


def human_years(species, age_years):
    """Return an animal's age in human years, using the shelter's poster.

    Works for dogs and cats. Returns None for any other species,
    because the poster has no rule for them.
    """
    if species == "Dog":
        per_later_year = 5
    elif species == "Cat":
        per_later_year = 4
    else:
        return None

    if age_years < 1:
        years = age_years * 15
    elif age_years < 2:
        years = 15 + (age_years - 1) * 9
    else:
        years = 15 + 9 + (age_years - 2) * per_later_year
    return round(years, 1)


def ask_pet():
    """Ask for a pet's name, species and age. Return all three."""
    name = input("Pet's name: ").strip()
    species = input("Species (Dog or Cat): ").strip().capitalize()
    age_years = float(input("Age in years: "))
    return name, species, age_years


def main():
    name, species, age_years = ask_pet()
    years = human_years(species, age_years)
    if years is None:
        print(f"Sorry, the poster has no rule for a {species.lower()}.")
    else:
        print(f"{name} is {years} in human years.")


if __name__ == "__main__":
    main()
