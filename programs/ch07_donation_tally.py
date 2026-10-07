# programs/ch07_donation_tally.py
# Add up donations typed in one at a time. A blank line finishes.

print("Sunny Paws donation tally")
print("Type each donation in whole dollars.")
print("Press Enter on a blank line when you are done.")
print()

total = 0
count = 0
largest = 0

while True:
    text = input("Donation: $").strip()
    if text == "":
        break
    if not text.isdigit():
        print("  Please type a whole number of dollars, like 25.")
        continue
    amount = int(text)
    total += amount
    count += 1
    if amount > largest:
        largest = amount

print()
if count == 0:
    print("No donations recorded.")
else:
    print(f"Donations: {count}")
    print(f"Total:     ${total:,}")
    print(f"Largest:   ${largest:,}")
    print(f"Average:   ${total / count:,.2f}")
