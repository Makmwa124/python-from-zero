# programs/shelter_manager/rules.py
"""The Sunny Paws rules: human years, adoption fees, food and Adoption Day."""

SPECIES = ["Dog", "Cat", "Rabbit", "Guinea pig"]
BASE_FEES = {"Dog": 150, "Cat": 90, "Rabbit": 45, "Guinea pig": 25}
LATER_YEARS = {"Dog": 5, "Cat": 4}
SENIOR_AGE = 8


def human_years(species, age_years):
    """Return a dog's or cat's age in human years (the shelter's poster)."""
    if species not in LATER_YEARS:
        raise ValueError(f"No human-years rule for {species}")
    if age_years < 0:
        raise ValueError("Age cannot be negative")
    if age_years < 1:
        return round(age_years * 15, 1)
    if age_years < 2:
        return round(15 + (age_years - 1) * 9, 1)
    return round(24 + (age_years - 2) * LATER_YEARS[species], 1)


def is_senior(species, age_years):
    """Return True for dogs and cats aged 8 or older."""
    return species in ("Dog", "Cat") and age_years >= SENIOR_AGE


def adoption_fee(species, age_years, status, adoption_day=False):
    """Return the adoption fee in dollars for one animal."""
    if species not in BASE_FEES:
        raise ValueError(f"Unknown species: {species}")
    if status == "Medical hold":
        raise ValueError("Animals on medical hold cannot be adopted")
    if adoption_day:
        return 0
    fee = BASE_FEES[species]
    if is_senior(species, age_years):
        fee = fee // 2
    return fee


def food_grams(species, age_years, weight_kg):
    """Return grams of dry food (or pellets) per day for one animal."""
    if species == "Dog":
        return round(weight_kg * 15)
    if species == "Cat":
        if age_years < 1:
            return 80
        return 60
    if species == "Rabbit":
        return 80
    if species == "Guinea pig":
        return 40
    raise ValueError(f"Unknown species: {species}")


def is_adoption_day(day):
    """True if day (a date) is Adoption Day, October's first Saturday."""
    return day.month == 10 and day.weekday() == 5 and day.day <= 7
