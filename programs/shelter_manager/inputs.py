# programs/shelter_manager/inputs.py
"""Input helpers that keep asking until the answer makes sense."""


def ask_text(prompt, allow_blank=False):
    """Ask for text; refuse a blank answer unless allow_blank is True."""
    while True:
        answer = input(prompt).strip()
        if answer or allow_blank:
            return answer
        print("  Please type something.")


def ask_number(prompt, minimum, maximum):
    """Ask for a number from minimum to maximum (decimals allowed)."""
    while True:
        answer = input(prompt).strip()
        try:
            number = float(answer)
        except ValueError:
            print(f"  '{answer}' is not a number. Try something like 2.5.")
            continue
        if minimum <= number <= maximum:
            return number
        print(f"  Please enter a number from {minimum} to {maximum}.")


def ask_int(prompt, minimum, maximum):
    """Ask for a whole number from minimum to maximum."""
    message = f"  Please enter a whole number from {minimum} to {maximum}."
    while True:
        answer = input(prompt).strip()
        try:
            number = int(answer)
        except ValueError:
            print(message)
            continue
        if minimum <= number <= maximum:
            return number
        print(message)


def ask_choice(prompt, choices):
    """Ask until the answer matches one of choices (any capitals).

    Returns the choice exactly as written in the list, so "guinea PIG"
    comes back as "Guinea pig".
    """
    while True:
        answer = input(prompt).strip().lower()
        for choice in choices:
            if answer == choice.lower():
                return choice
        print(f"  Please choose one of: {', '.join(choices)}.")


def ask_yes_no(prompt):
    """Ask a yes/no question; return True for yes."""
    answer = ask_choice(prompt, ["y", "n", "yes", "no"])
    return answer in ("y", "yes")
