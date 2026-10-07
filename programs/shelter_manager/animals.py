# programs/shelter_manager/animals.py
"""The Animal and Shelter classes for the Sunny Paws Shelter Manager."""
import rules

# Where each species sleeps, and how many of those spaces the shelter has.
SPACE_FOR = {"Dog": "kennels", "Cat": "condos",
             "Rabbit": "hutches", "Guinea pig": "hutches"}
SPACES = {"kennels": 20, "condos": 16, "hutches": 8}
ON_SITE = ("Available", "Medical hold")   # Foster animals live elsewhere
CAN_ADOPT = ("Available", "Foster")


class Animal:
    """One animal in the shelter's care."""

    def __init__(self, animal_id, name, species, breed, sex, age_years,
                 weight_kg, arrived, status="Available", adopted_on="",
                 good_with_kids=False, notes=""):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.breed = breed
        self.sex = sex
        self.age_years = age_years
        self.weight_kg = weight_kg
        self.arrived = arrived            # text such as "2026-01-07"
        self.status = status
        self.adopted_on = adopted_on      # "" until adopted
        self.good_with_kids = good_with_kids
        self.notes = notes

    def __str__(self):
        return (f"{self.animal_id} {self.name}, {self.species} "
                f"({self.breed}), {self.age_years} years, {self.status}")

    def human_years(self):
        """Age in human years, or None for species without a rule."""
        if self.species in ("Dog", "Cat"):
            return rules.human_years(self.species, self.age_years)
        return None

    def can_be_adopted(self):
        return self.status in CAN_ADOPT

    def fee(self, adoption_day=False):
        return rules.adoption_fee(self.species, self.age_years,
                                  self.status, adoption_day)

    def daily_food(self):
        return rules.food_grams(self.species, self.age_years,
                                self.weight_kg)

    def matches(self, text):
        """True if text appears in the ID, name, species, breed or notes."""
        text = text.strip().lower()
        haystack = " ".join([self.animal_id, self.name, self.species,
                             self.breed, self.notes]).lower()
        return text in haystack

    def to_dict(self):
        """The animal as a plain dict, ready to save as JSON."""
        return {
            "id": self.animal_id, "name": self.name,
            "species": self.species, "breed": self.breed, "sex": self.sex,
            "age_years": self.age_years, "weight_kg": self.weight_kg,
            "arrived": self.arrived, "status": self.status,
            "adopted_on": self.adopted_on,
            "good_with_kids": self.good_with_kids, "notes": self.notes,
        }


class Shelter:
    """The whole shelter: its animals and its donations."""

    def __init__(self, name="Sunny Paws Animal Rescue"):
        self.name = name
        self.animals = []
        self.donations = []

    def add(self, animal):
        self.animals.append(animal)

    def find(self, animal_id):
        """Return the animal with this ID, or None if there is none."""
        animal_id = animal_id.strip().upper()
        for animal in self.animals:
            if animal.animal_id == animal_id:
                return animal
        return None

    def search(self, text):
        return [animal for animal in self.animals if animal.matches(text)]

    def with_status(self, status):
        if status == "All":
            return list(self.animals)
        return [animal for animal in self.animals if animal.status == status]

    def next_id(self):
        """The next free ID, one higher than the highest so far."""
        highest = 0
        for animal in self.animals:
            number = int(animal.animal_id.split("-")[1])
            highest = max(highest, number)
        return f"SP-{highest + 1:03d}"

    def spaces_free(self, species):
        """How many kennels, condos or hutches are free for this species."""
        space = SPACE_FOR[species]
        used = 0
        for animal in self.animals:
            if SPACE_FOR[animal.species] == space and animal.status in ON_SITE:
                used += 1
        return SPACES[space] - used

    def adopt(self, animal_id, day):
        """Record an adoption on day (a date) and return the fee charged."""
        animal = self.find(animal_id)
        if animal is None:
            raise ValueError(f"No animal with ID {animal_id}")
        if animal.status == "Adopted":
            raise ValueError(f"{animal.name} has already been adopted")
        if animal.status == "Medical hold":
            raise ValueError(f"{animal.name} is on medical hold and "
                             "cannot be adopted yet")
        fee = animal.fee(adoption_day=rules.is_adoption_day(day))
        animal.status = "Adopted"
        animal.adopted_on = day.isoformat()
        return fee
