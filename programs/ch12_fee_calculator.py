# programs/ch12_fee_calculator.py
"""Sunny Paws adoption fee calculator that survives unexpected answers."""
from ch12_input_helpers import ask_choice, ask_number
from shelter_tools import adoption_fee

SPECIES = ["Dog", "Cat", "Rabbit", "Guinea pig"]
STATUSES = ["Available", "Foster", "Medical hold"]


def main():
    print("Sunny Paws adoption fee calculator")
    print()
    name = input("Animal's name: ").strip()
    species = ask_choice("Species (Dog, Cat, Rabbit, Guinea pig): ", SPECIES)
    age_years = ask_number("Age in years: ", minimum=0, maximum=30)
    status = ask_choice("Status (Available, Foster, Medical hold): ",
                        STATUSES)
    fee = adoption_fee(species, age_years, status)
    if fee is None:
        print(f"Sorry, {name} cannot be adopted right now.")
        return
    donation = ask_number("Optional donation in dollars (0 for none): ",
                          minimum=0)
    print()
    print(f"Receipt for {name}")
    print(f"Adoption fee:  ${fee:>7.2f}")
    print(f"Donation:      ${donation:>7.2f}")
    print(f"Total:         ${fee + donation:>7.2f}")


if __name__ == "__main__":
    main()
