# programs/ch12_input_helpers.py
"""Input helpers that keep asking until the answer makes sense.

Import them into any program, for example:

    from ch12_input_helpers import ask_choice, ask_int, ask_number
"""


def ask_number(prompt, minimum=None, maximum=None):
    """Ask until the user types a number in range. Return it as a float.

    minimum and maximum are optional limits (both included).
    """
    while True:
        text = input(prompt).strip()
        try:
            number = float(text)
        except ValueError:
            print(f"Sorry, '{text}' is not a number. "
                  "Please type digits, like 4 or 4.5.")
            continue
        if minimum is not None and number < minimum:
            print(f"Please enter a number of at least {minimum}.")
        elif maximum is not None and number > maximum:
            print(f"Please enter a number no bigger than {maximum}.")
        else:
            return number


def ask_int(prompt, minimum=None, maximum=None):
    """Ask until the user types a whole number in range. Return an int.

    minimum and maximum are optional limits (both included).
    """
    while True:
        text = input(prompt).strip()
        try:
            number = int(text)
        except ValueError:
            print(f"Sorry, '{text}' is not a whole number. "
                  "Please type digits only, like 3.")
            continue
        if minimum is not None and number < minimum:
            print(f"Please enter a whole number of at least {minimum}.")
        elif maximum is not None and number > maximum:
            print(f"Please enter a whole number no bigger than {maximum}.")
        else:
            return number


def ask_choice(prompt, choices):
    """Ask until the answer matches one of choices (any capitals).

    Returns the matching item from choices, spelled as it is there.
    """
    while True:
        text = input(prompt).strip()
        for choice in choices:
            if text.lower() == choice.lower():
                return choice
        print(f"Sorry, '{text}' is not an option. "
              f"Choose from: {', '.join(choices)}.")


if __name__ == "__main__":
    # Try the helpers out when this file is run directly.
    age = ask_number("Age in years: ", minimum=0, maximum=30)
    print("You typed", age)
    count = ask_int("How many animals? ", minimum=1, maximum=10)
    print("You typed", count)
    species = ask_choice("Species: ", ["Dog", "Cat", "Rabbit", "Guinea pig"])
    print("You chose", species)
