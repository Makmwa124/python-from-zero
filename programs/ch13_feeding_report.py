# programs/ch13_feeding_report.py
"""Write the daily feeding report for every animal still at Sunny Paws.

Run this from the programs folder. It reads ../data/animals.csv and saves
the report to output/feeding_report.txt.
"""
import csv
from pathlib import Path

DATA_FILE = Path("../data/animals.csv")
OUTPUT_FOLDER = Path("output")
REPORT_FILE = OUTPUT_FOLDER / "feeding_report.txt"


def food_plan(species, age_years, weight_kg):
    """Return (grams of dry food or pellets, how to serve it) for one animal."""
    if species == "Dog":
        grams = round(weight_kg * 15)
        if age_years < 1:
            return grams, "dry food, three times a day"
        return grams, "dry food, morning and evening"
    if species == "Cat":
        if age_years < 1:
            return 80, "dry food, four small meals"
        return 60, "dry food, morning and evening"
    if species == "Rabbit":
        return 80, "pellets, plus unlimited hay"
    return 40, "pellets, plus hay and fresh veg"


def load_animals(path):
    """Read the CSV file and return a list of dictionaries, one per animal."""
    with open(path, encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def main():
    animals = load_animals(DATA_FILE)
    report_lines = ["Sunny Paws daily feeding report", ""]
    total_dry_food = 0
    fed = 0
    for animal in animals:
        if animal["status"] == "Adopted":
            continue
        age = float(animal["age_years"])
        weight = float(animal["weight_kg"])
        grams, how = food_plan(animal["species"], age, weight)
        if animal["species"] in ("Dog", "Cat"):
            total_dry_food += grams
        fed += 1
        report_lines.append(
            f"{animal['id']}  {animal['name']:<9}{animal['species']:<12}"
            f"{grams:>4} g {how}"
        )
    report_lines.append("")
    report_lines.append(f"Animals to feed: {fed}")
    report_lines.append(f"Dry food for dogs and cats: {total_dry_food:,} g")

    OUTPUT_FOLDER.mkdir(exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        for line in report_lines:
            file.write(line + "\n")
    print(f"Read {len(animals)} animals from {DATA_FILE}")
    print(f"Wrote {len(report_lines)} lines to {REPORT_FILE}")


if __name__ == "__main__":
    main()
