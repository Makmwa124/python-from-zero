# programs/shelter_tools.py
"""Sunny Paws Animal Rescue: shared tools for the shelter's programs.

Import what you need, for example:

    from shelter_tools import adoption_fee, food_grams, human_years
"""

SHELTER_NAME = "Sunny Paws Animal Rescue"


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


def adoption_fee(species, age_years, status):
    """Return the adoption fee in dollars for one animal.

    Dogs and cats aged 8 or older (seniors) pay half price.
    Returns None if the animal is on medical hold (it cannot be
    adopted yet) or if the species is not one the shelter takes.
    """
    if status == "Medical hold":
        return None
    fees = {"Dog": 150, "Cat": 90, "Rabbit": 45, "Guinea pig": 25}
    if species not in fees:
        return None
    fee = fees[species]
    if species in ("Dog", "Cat") and age_years >= 8:
        fee = fee // 2
    return fee


def food_grams(species, age_years, weight_kg):
    """Return grams of dry food (or pellets) per day for one animal.

    Dogs: 15 g per kg of body weight, rounded. Cats: 60 g, or 80 g
    for kittens under 1 year. Rabbits: 80 g of pellets. Guinea pigs:
    40 g of pellets. Returns None for any other species.
    """
    if species == "Dog":
        return round(weight_kg * 15)
    elif species == "Cat":
        if age_years < 1:
            return 80
        return 60
    elif species == "Rabbit":
        return 80
    elif species == "Guinea pig":
        return 40
    return None


def feeding_plan(species, age_years, weight_kg):
    """Return (grams per day, how to feed) for one animal."""
    grams = food_grams(species, age_years, weight_kg)
    if species == "Dog":
        if age_years < 1:
            how = "three times a day"
        else:
            how = "morning and evening"
    elif species == "Cat":
        if age_years < 1:
            how = "four small meals"
        else:
            how = "morning and evening"
    elif species == "Rabbit":
        how = "pellets, plus unlimited hay"
    else:
        how = "pellets, plus hay and fresh veg"
    return grams, how


if __name__ == "__main__":
    # Quick self-check: runs only when this file is run directly.
    print(f"{SHELTER_NAME}: shelter_tools self-check")
    print("Dog, 3 years:", human_years("Dog", 3), "human years")
    print("Cat, 3 years:", human_years("Cat", 3), "human years")
    print("Senior dog fee:", adoption_fee("Dog", 10, "Available"))
    print("Peanut's food:", food_grams("Dog", 4.5, 28.6), "g")
