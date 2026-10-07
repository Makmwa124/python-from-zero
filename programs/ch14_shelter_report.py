# programs/ch14_shelter_report.py
"""Print an adoption report using the classes in ch14_animals.py.

Run it from the programs folder, next to ch14_animals.py.
"""
from ch14_animals import Shelter


def main():
    shelter = Shelter("Sunny Paws Animal Rescue")
    shelter.load_csv("../data/animals.csv")
    print(shelter)
    for species, count in shelter.species_counts().items():
        print(f"  {species:<11}{count:>3}")

    print()
    print("Ready for a new home (* = senior, half price):")
    total = 0
    for animal in shelter.adoptable():
        fee = animal.adoption_fee()
        total += fee
        marker = ""
        if animal.is_senior():
            marker = "*"
        print(f"  {animal.animal_id}  {animal.name:<9}{animal.species:<12}"
              f"${fee:>4}{marker}")
    print(f"Fees if every one of them finds a home: ${total:,}")


if __name__ == "__main__":
    main()
