# programs/ch11_volunteer_tools.py
"""Small helpers for the Sunny Paws volunteer rota."""

OPEN_DAYS = ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def is_open_day(day_name):
    """Return True if the shelter is open on this day ("Mon" to "Sun")."""
    return day_name in OPEN_DAYS


if __name__ == "__main__":
    # Self-check: runs only when this file is run directly.
    print("Mon open?", is_open_day("Mon"))
    print("Sat open?", is_open_day("Sat"))
