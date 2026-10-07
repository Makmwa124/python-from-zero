# programs/shelter_manager/main.py
"""The Sunny Paws Shelter Manager.

Run from the programs/shelter_manager folder:
    python3 main.py      (macOS and Linux)
    py main.py           (Windows)
"""
from datetime import date

import storage
from animals import Animal
from inputs import ask_choice, ask_int, ask_number, ask_text, ask_yes_no
from reports import (animal_card, animal_table, donations_summary,
                     export_report)
from rules import SPECIES, is_adoption_day, is_senior

MENU = """
=== Sunny Paws Shelter Manager ===
1) List animals   2) Search         3) Add an animal
4) Adopt          5) Donations      6) Export report
7) Save           8) Quit"""

STATUSES = ["Available", "Foster", "Medical hold", "Adopted", "All"]


def list_animals(shelter):
    status = ask_choice("Which status? (Available, Foster, Medical hold, "
                        "Adopted, All) ", STATUSES)
    animals = shelter.with_status(status)
    print(animal_table(animals))
    print(f"{len(animals)} animals.")


def search_animals(shelter):
    text = ask_text("Search for (name, breed, ID or note): ")
    found = shelter.search(text)
    if not found:
        print(f"No animals match '{text}'.")
        return
    print(animal_table(found))
    animal_id = ask_text("ID for details (or press Enter to go back): ",
                         allow_blank=True)
    if animal_id:
        animal = shelter.find(animal_id)
        if animal is None:
            print(f"No animal with ID {animal_id}.")
        else:
            print(animal_card(animal))


def add_animal(shelter, today):
    """Ask for a new animal's details and add it. Return True if added."""
    species = ask_choice("Species (Dog, Cat, Rabbit, Guinea pig): ", SPECIES)
    free = shelter.spaces_free(species)
    if free <= 0:
        print(f"Sorry, there is no free space for a {species.lower()} "
              "right now.")
        return False
    print(f"  ({free} spaces free for this species)")
    name = ask_text("Name: ").title()
    breed = ask_text("Breed (Enter if unknown): ", allow_blank=True)
    sex = ask_choice("Sex (F/M): ", ["F", "M"])
    age = ask_number("Age in years (for example 2.5): ", 0, 30)
    weight = ask_number("Weight in kg: ", 0.1, 100)
    good_with_kids = ask_yes_no("Good with kids? (y/n) ")
    notes = ask_text("Notes (Enter for none): ", allow_blank=True)
    animal = Animal(shelter.next_id(), name, species, breed or "Unknown",
                    sex, age, weight, today.isoformat(),
                    good_with_kids=good_with_kids, notes=notes)
    shelter.add(animal)
    print(f"Added {animal}.")
    return True


def record_adoption(shelter, today):
    """Record an adoption. Return True if one was recorded."""
    animal_id = ask_text("ID of the animal being adopted: ")
    animal = shelter.find(animal_id)
    if animal is None:
        print(f"No animal with ID {animal_id}.")
        return False
    if not animal.can_be_adopted():
        if animal.status == "Adopted":
            print(f"{animal.name} has already been adopted.")
        else:
            print(f"Sorry, {animal.name} is on medical hold and cannot be "
                  "adopted yet.")
        return False
    adoption_day = is_adoption_day(today)
    fee = animal.fee(adoption_day)
    if adoption_day:
        print("It's Adoption Day: all fees are waived!")
    print(f"{animal.name} the {animal.species.lower()}, "
          f"{animal.age_years} years old. Adoption fee: ${fee}")
    if is_senior(animal.species, animal.age_years) and not adoption_day:
        print("(Senior pet: half the usual fee.)")
    if not ask_yes_no("Confirm the adoption? (y/n) "):
        print("Nothing changed.")
        return False
    shelter.adopt(animal.animal_id, today)
    print(f"Done! {animal.name} was adopted on {animal.adopted_on}. "
          f"Collect ${fee}.")
    return True


def main():
    try:
        shelter, message = storage.start_shelter()
    except (OSError, ValueError) as error:
        print(f"Could not load the shelter's data: {error}")
        return
    print(message)
    today = date.today()
    unsaved = False

    while True:
        print(MENU)
        choice = ask_int("Choose 1-8: ", 1, 8)
        print()
        if choice == 1:
            list_animals(shelter)
        elif choice == 2:
            search_animals(shelter)
        elif choice == 3:
            if add_animal(shelter, today):
                unsaved = True
        elif choice == 4:
            if record_adoption(shelter, today):
                unsaved = True
        elif choice == 5:
            print(donations_summary(shelter.donations))
        elif choice == 6:
            path = export_report(shelter, today, storage.HERE / "output")
            print(f"Report written to output/{path.name}")
        elif choice == 7:
            storage.save_shelter(shelter)
            unsaved = False
            print(f"Saved {len(shelter.animals)} animals and "
                  f"{len(shelter.donations)} donations to "
                  f"{storage.SAVE_FILE.name}.")
        elif choice == 8:
            if unsaved and ask_yes_no("Save your changes first? (y/n) "):
                storage.save_shelter(shelter)
                print(f"Saved to {storage.SAVE_FILE.name}.")
            print("Goodbye from Sunny Paws!")
            break


if __name__ == "__main__":
    main()
