# programs/ch14_animals.py
"""Animal, Dog, Cat and Shelter classes for Sunny Paws (Chapter 14).

Run it from the programs folder to see a short demo, or import the classes
into another program with:  from ch14_animals import Shelter
"""
import csv

FEES = {"Dog": 150, "Cat": 90, "Rabbit": 45, "Guinea pig": 25}


class Animal:
    """One animal at Sunny Paws."""

    def __init__(self, animal_id, name, species, breed, age_years,
                 weight_kg, status="Available", good_with_kids=False):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.breed = breed
        self.age_years = age_years
        self.weight_kg = weight_kg
        self.status = status
        self.good_with_kids = good_with_kids
        self.adopted_on = ""

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age_years} years)"

    def human_years(self):
        """The poster only has rules for dogs and cats."""
        return None

    def food_grams(self):
        """Grams of pellets per day for a rabbit or guinea pig."""
        if self.species == "Rabbit":
            return 80
        return 40

    def is_senior(self):
        return self.species in ("Dog", "Cat") and self.age_years >= 8

    def is_adoptable(self):
        return self.status in ("Available", "Foster")

    def adoption_fee(self):
        """The fee in dollars, or None if the animal cannot be adopted."""
        if not self.is_adoptable():
            return None
        fee = FEES[self.species]
        if self.is_senior():
            fee = fee // 2
        return fee

    def adopt(self, date):
        """Record an adoption on the given date (text like "2026-07-04")."""
        if not self.is_adoptable():
            raise ValueError(f"{self.name} cannot be adopted ({self.status})")
        self.status = "Adopted"
        self.adopted_on = date


class Dog(Animal):
    """A dog: uses the dog rules for human years and food."""

    def __init__(self, animal_id, name, breed, age_years, weight_kg,
                 status="Available", good_with_kids=False):
        super().__init__(animal_id, name, "Dog", breed, age_years,
                         weight_kg, status, good_with_kids)

    def human_years(self):
        if self.age_years < 1:
            years = self.age_years * 15
        elif self.age_years < 2:
            years = 15 + (self.age_years - 1) * 9
        else:
            years = 15 + 9 + (self.age_years - 2) * 5
        return round(years, 1)

    def food_grams(self):
        return round(self.weight_kg * 15)


class Cat(Animal):
    """A cat: uses the cat rules for human years and food."""

    def __init__(self, animal_id, name, breed, age_years, weight_kg,
                 status="Available", good_with_kids=False):
        super().__init__(animal_id, name, "Cat", breed, age_years,
                         weight_kg, status, good_with_kids)

    def human_years(self):
        if self.age_years < 1:
            years = self.age_years * 15
        elif self.age_years < 2:
            years = 15 + (self.age_years - 1) * 9
        else:
            years = 15 + 9 + (self.age_years - 2) * 4
        return round(years, 1)

    def food_grams(self):
        if self.age_years < 1:
            return 80
        return 60


def make_animal(row):
    """Turn one row from animals.csv (a dict of strings) into an object."""
    age = float(row["age_years"])
    weight = float(row["weight_kg"])
    kids = row["good_with_kids"] == "yes"
    if row["species"] == "Dog":
        animal = Dog(row["id"], row["name"], row["breed"], age, weight,
                     row["status"], kids)
    elif row["species"] == "Cat":
        animal = Cat(row["id"], row["name"], row["breed"], age, weight,
                     row["status"], kids)
    else:
        animal = Animal(row["id"], row["name"], row["species"], row["breed"],
                        age, weight, row["status"], kids)
    animal.adopted_on = row["adopted_on"]
    return animal


class Shelter:
    """A shelter holds a list of Animal objects."""

    def __init__(self, name):
        self.name = name
        self.animals = []

    def __str__(self):
        return f"{self.name} ({len(self.animals)} animals)"

    def add(self, animal):
        self.animals.append(animal)

    def load_csv(self, path):
        """Add every animal in a CSV file like data/animals.csv."""
        with open(path, encoding="utf-8", newline="") as file:
            for row in csv.DictReader(file):
                self.add(make_animal(row))

    def find(self, animal_id):
        """Return the animal with this id, or None."""
        for animal in self.animals:
            if animal.animal_id == animal_id:
                return animal
        return None

    def adoptable(self, species=None):
        """Animals that can be adopted, optionally of one species only."""
        found = []
        for animal in self.animals:
            if animal.is_adoptable():
                if species is None or animal.species == species:
                    found.append(animal)
        return found

    def species_counts(self):
        counts = {}
        for animal in self.animals:
            counts[animal.species] = counts.get(animal.species, 0) + 1
        return counts


def main():
    shelter = Shelter("Sunny Paws Animal Rescue")
    shelter.load_csv("../data/animals.csv")
    print(shelter)
    for animal_id in ["SP-001", "SP-009", "SP-016"]:
        animal = shelter.find(animal_id)
        print(f"{animal}: {animal.human_years()} human years, "
              f"fee ${animal.adoption_fee()}, {animal.food_grams()} g a day")


if __name__ == "__main__":
    main()
