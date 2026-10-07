# programs/ch07_menu.py
# A small menu-driven helper for Sunny Paws volunteers.

print("=== Sunny Paws helper ===")

while True:
    print()
    print("1. Opening hours")
    print("2. Adoption fee")
    print("3. Daily food for a dog")
    print("4. Quit")
    choice = input("Choose 1 to 4: ").strip()

    if choice == "1":
        print("Open Tuesday to Sunday, 10:00 to 17:00. Closed Mondays.")

    elif choice == "2":
        species = input("Species: ").strip().lower()
        if species == "dog":
            fee = 150
        elif species == "cat":
            fee = 90
        elif species == "rabbit":
            fee = 45
        elif species == "guinea pig":
            fee = 25
        else:
            print("Sorry, Sunny Paws doesn't have that species.")
            continue
        age = float(input("Age in years: "))
        if (species == "dog" or species == "cat") and age >= 8:
            fee = fee / 2
            print("Senior pet: half price!")
        print(f"Adoption fee: ${fee:.2f}")

    elif choice == "3":
        weight = float(input("Dog's weight in kg: "))
        grams = round(weight * 15)
        morning = grams // 2
        evening = grams - morning
        print(f"{grams} g of dry food a day: {morning} g in the morning "
              f"and {evening} g in the evening.")

    elif choice == "4":
        print("Goodbye, and thanks for helping!")
        break

    else:
        print(f"Sorry, '{choice}' is not on the menu. Please type 1 to 4.")
