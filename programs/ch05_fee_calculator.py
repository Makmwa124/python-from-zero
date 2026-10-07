# programs/ch05_fee_calculator.py
# Adoption fee calculator, version 1: cats only, plus an optional donation.

cat_fee = 90

print("Sunny Paws adoption fee calculator")
print(f"The adoption fee is ${cat_fee} per cat.")
print()

# Input
adopter = input("Adopter's name: ").strip().title()
cats = int(input("How many cats are being adopted? "))
donation = float(input("Extra donation in dollars (0 for none): "))

# Process
fees = cats * cat_fee
total = fees + donation

# Output
print()
print("=" * 32)
print(f"{'SUNNY PAWS RECEIPT':^32}")
print("=" * 32)
print(f"Adopter:        {adopter}")
print(f"Cats adopted:   {cats}")
print(f"Adoption fees:  ${fees:>10.2f}")
print(f"Donation:       ${donation:>10.2f}")
print("-" * 32)
print(f"Total to pay:   ${total:>10.2f}")
print("=" * 32)
print("Thank you for giving a cat a home!")
