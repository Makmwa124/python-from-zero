# programs/shelter_manager/storage.py
"""Loading and saving the shelter's data (CSV in, JSON in and out)."""
import csv
import json
from pathlib import Path

from animals import Animal, Shelter

HERE = Path(__file__).parent              # the shelter_manager folder
DATA = HERE.parent.parent / "data"         # the book's data folder
SAVE_FILE = HERE / "shelter_data.json"


def animal_from_dict(row):
    """Build an Animal from a CSV row or a saved dict (same keys)."""
    return Animal(
        animal_id=row["id"],
        name=row["name"],
        species=row["species"],
        breed=row["breed"],
        sex=row["sex"],
        age_years=float(row["age_years"]),
        weight_kg=float(row["weight_kg"]),
        arrived=row["arrived"],
        status=row["status"],
        adopted_on=row["adopted_on"],
        good_with_kids=row["good_with_kids"] in (True, "yes"),
        notes=row["notes"],
    )


def load_animals_csv(path):
    with open(path, encoding="utf-8", newline="") as file:
        return [animal_from_dict(row) for row in csv.DictReader(file)]


def load_donations_csv(path):
    donations = []
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            row["amount"] = int(row["amount"])
            donations.append(row)
    return donations


def save_shelter(shelter, path=SAVE_FILE):
    """Save every animal and donation to a JSON file."""
    data = {
        "shelter": shelter.name,
        "animals": [animal.to_dict() for animal in shelter.animals],
        "donations": shelter.donations,
    }
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_shelter(path=SAVE_FILE):
    """Load a shelter saved by save_shelter()."""
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    shelter = Shelter(data["shelter"])
    for row in data["animals"]:
        shelter.add(animal_from_dict(row))
    shelter.donations = data["donations"]
    return shelter


def start_shelter(save_file=SAVE_FILE, data_folder=DATA):
    """Load the saved shelter, or import the CSV files the first time.

    Returns the shelter and a message saying where the data came from.
    """
    if Path(save_file).exists():
        shelter = load_shelter(save_file)
        source = Path(save_file).name
    else:
        shelter = Shelter()
        for animal in load_animals_csv(Path(data_folder) / "animals.csv"):
            shelter.add(animal)
        shelter.donations = load_donations_csv(
            Path(data_folder) / "donations.csv")
        source = "the CSV files (no saved file yet)"
    message = (f"Loaded {len(shelter.animals)} animals and "
               f"{len(shelter.donations)} donations from {source}.")
    return shelter, message
