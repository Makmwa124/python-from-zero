# programs/ch05_pet_age.py
# Converts a dog's age into human years, using the shelter's poster:
# 15 for the first year, 9 for the second, then 5 for each year after.
# This version only works for dogs aged 2 or older (Chapter 6 fixes that).

print("Sunny Paws pet age converter (dogs aged 2 and up)")
print()

# Input
name = input("What is the dog's name? ").strip().title()
age = float(input(f"How old is {name}, in years? "))

# Process
human_years = 15 + 9 + (age - 2) * 5

# Output
print()
print(f"{name} is {age} years old.")
print(f"That is about {human_years:.1f} in human years.")
