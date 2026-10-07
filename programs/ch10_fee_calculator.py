# programs/ch10_fee_calculator.py
"""Sunny Paws adoption fee calculator, rebuilt with functions."""


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


def print_banner():
    """Print the program's title."""
    print("=" * 36)
    print("  Sunny Paws adoption fee calculator")
    print("=" * 36)


def ask_animal():
    """Ask about one animal. Return (name, species, age, status)."""
    name = input("Animal's name: ").strip()
    species_prompt = "Species (Dog, Cat, Rabbit, Guinea pig): "
    species = input(species_prompt).strip().capitalize()
    age_years = float(input("Age in years: "))
    status_prompt = "Status (Available, Foster, Medical hold): "
    status = input(status_prompt).strip().capitalize()
    return name, species, age_years, status


def print_receipt(name, fee, donation):
    """Print the fee, the donation and the total."""
    print()
    print(f"Receipt for {name}")
    print(f"Adoption fee:  ${fee:>7.2f}")
    print(f"Donation:      ${donation:>7.2f}")
    print(f"Total:         ${fee + donation:>7.2f}")
    print("Thank you for adopting from Sunny Paws!")


def main():
    print_banner()
    name, species, age_years, status = ask_animal()
    fee = adoption_fee(species, age_years, status)
    if fee is None:
        print(f"Sorry, {name} cannot be adopted right now.")
        return
    donation = float(input("Optional donation in dollars (0 for none): "))
    print_receipt(name, fee, donation)


if __name__ == "__main__":
    main()
