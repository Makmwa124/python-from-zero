# programs/ch10_feeding_plan.py
"""Print today's feeding plan for some of the Sunny Paws animals."""


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


def print_plan(animals):
    """Print one line per animal and return the total grams."""
    total = 0
    for animal in animals:
        grams, how = feeding_plan(animal["species"], animal["age_years"],
                                  animal["weight_kg"])
        print(f"{animal['name']:<8} {grams:>4} g  {how}")
        total += grams
    return total


def main():
    animals = [
        {"name": "Peanut", "species": "Dog", "age_years": 4.5,
         "weight_kg": 28.6},
        {"name": "Waffles", "species": "Cat", "age_years": 0.6,
         "weight_kg": 1.7},
        {"name": "Poppy", "species": "Dog", "age_years": 10,
         "weight_kg": 30.7},
        {"name": "Hazel", "species": "Rabbit", "age_years": 3,
         "weight_kg": 2.5},
        {"name": "Olive", "species": "Dog", "age_years": 0.9,
         "weight_kg": 6.8},
        {"name": "Pip", "species": "Guinea pig", "age_years": 2,
         "weight_kg": 1.1},
    ]
    print("Sunny Paws feeding plan")
    print("-" * 46)
    total = print_plan(animals)
    print("-" * 46)
    print(f"Total: {total} g ({total / 1000:.2f} kg)")


if __name__ == "__main__":
    main()
