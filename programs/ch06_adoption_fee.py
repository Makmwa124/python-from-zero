# programs/ch06_adoption_fee.py
# Adoption fee calculator, version 2: the shelter's real fee rules.
#   Dog $150, Cat $90, Rabbit $45, Guinea pig $25.
#   Dogs and cats aged 8 or older (seniors) pay half.
#   Animals on medical hold cannot be adopted.
#   On Adoption Day (first Saturday of October) all fees are waived.

print("Sunny Paws adoption fee calculator")
print()

# Input
name = input("Animal's name: ").strip().title()
species = input("Species (dog, cat, rabbit, guinea pig): ").strip().lower()
age = float(input(f"How old is {name}, in years? "))
status = input("Status (available, foster, medical hold, adopted): ")
status = status.strip().lower()
adoption_day = input("Is today Adoption Day? (yes/no): ").strip().lower()

# Process and output
print()
if status == "medical hold":
    print(f"Sorry, {name} is on medical hold and can't be adopted yet.")
    print("Please check again after Dr. Osei's next visit.")
elif status == "adopted":
    print(f"{name} has already found a home!")
else:
    if species == "dog":
        base_fee = 150
    elif species == "cat":
        base_fee = 90
    elif species == "rabbit":
        base_fee = 45
    elif species == "guinea pig":
        base_fee = 25
    else:
        base_fee = 0

    if base_fee == 0:
        print(f"Sorry, there is no fee rule for '{species}'.")
        print("Please ask Rosa.")
    else:
        is_senior = (species == "dog" or species == "cat") and age >= 8

        if adoption_day == "yes":
            fee = 0
            reason = "Adoption Day: all fees waived!"
        elif is_senior:
            fee = base_fee / 2
            reason = "Senior pet: half price."
        else:
            fee = base_fee
            reason = "Standard fee."

        print(f"Adoption fee for {name}: ${fee:.2f}")
        print(reason)
