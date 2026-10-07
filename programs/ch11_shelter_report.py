# programs/ch11_shelter_report.py
"""A short report on the available animals, using shelter_tools."""
import statistics

from ch11_animals import ANIMALS
from shelter_tools import SHELTER_NAME, adoption_fee, human_years


def main():
    print(SHELTER_NAME)
    print("Available animals report")
    print()
    print("Name     Species      Age  Human   Fee")
    for animal in ANIMALS:
        species = animal["species"]
        age = animal["age_years"]
        years = human_years(species, age)
        if years is None:
            years = "-"
        fee = adoption_fee(species, age, animal["status"])
        fee_text = f"${fee}"
        print(f"{animal['name']:<8} {species:<11} {age:>4} {years:>6} "
              f"{fee_text:>5}")

    ages = [animal["age_years"] for animal in ANIMALS]
    print()
    print(f"Animals:        {len(ages)}")
    print(f"Average age:    {statistics.mean(ages):.1f} years")
    print(f"Median age:     {statistics.median(ages)} years")
    fees = [adoption_fee(a["species"], a["age_years"], a["status"])
            for a in ANIMALS]
    print(f"If all adopted: ${sum(fees)} in fees")


if __name__ == "__main__":
    main()
