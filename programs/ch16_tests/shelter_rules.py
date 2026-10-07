# programs/ch16_tests/shelter_rules.py
"""The Sunny Paws rules: human years, adoption fees and daily food."""

BASE_FEES = {"Dog": 150, "Cat": 90, "Rabbit": 45, "Guinea pig": 25}
LATER_YEARS = {"Dog": 5, "Cat": 4}


def clean_species(species):
    """Return species with tidy capitals, so "dog " becomes "Dog"."""
    return species.strip().capitalize()


def human_years(species, age_years):
    """Return a dog's or cat's age in human years."""
    species = clean_species(species)
    if species not in LATER_YEARS:
        raise ValueError(f"No human-years rule for {species}")
    if age_years < 0:
        raise ValueError("Age cannot be negative")
    if age_years < 1:
        return round(age_years * 15, 1)
    if age_years < 2:
        return round(15 + (age_years - 1) * 9, 1)
    return round(24 + (age_years - 2) * LATER_YEARS[species], 1)


def adoption_fee(species, age_years, status):
    """Return the adoption fee in dollars for one animal."""
    species = clean_species(species)
    if species not in BASE_FEES:
        raise ValueError(f"Unknown species: {species}")
    if status == "Medical hold":
        raise ValueError("Animals on medical hold cannot be adopted")
    fee = BASE_FEES[species]
    if species in ("Dog", "Cat") and age_years >= 8:
        fee = fee // 2
    return fee


def food_grams(species, age_years, weight_kg):
    """Return grams of dry food (or pellets) per day for one animal."""
    species = clean_species(species)
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
