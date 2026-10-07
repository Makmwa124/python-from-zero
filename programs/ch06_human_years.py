# programs/ch06_human_years.py
# Converts a dog's or cat's age into human years, using the shelter's poster:
#   First year: 15. Second year: 9 more.
#   After that: 5 per year for dogs, 4 per year for cats.
#   Under one year: age * 15.

print("Sunny Paws human years calculator")
print()

# Input
name = input("Pet's name: ").strip().title()
species = input("Dog or cat? ").strip().lower()
age = float(input(f"How old is {name}, in years? "))

# Process and output
print()
if species != "dog" and species != "cat":
    print("Sorry, the poster only covers dogs and cats.")
elif age < 0:
    print("An age can't be negative. Please check and try again.")
else:
    if species == "dog":
        per_later_year = 5
    else:
        per_later_year = 4

    if age < 1:
        human_years = age * 15
    elif age < 2:
        human_years = 15 + (age - 1) * 9
    else:
        human_years = 15 + 9 + (age - 2) * per_later_year

    print(f"{name} the {species} is {age} years old.")
    print(f"That is about {human_years:.1f} in human years.")
