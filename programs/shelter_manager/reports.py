# programs/shelter_manager/reports.py
"""Tables and reports for the Sunny Paws Shelter Manager."""
from datetime import date

from animals import ON_SITE, SPACE_FOR, SPACES

MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def animal_table(animals):
    """Return a neat text table of animals, one per line."""
    lines = [f"{'ID':<8}{'Name':<10}{'Species':<12}{'Age':>5}  Status",
             "-" * 47]
    for animal in animals:
        lines.append(f"{animal.animal_id:<8}{animal.name:<10}"
                     f"{animal.species:<12}{animal.age_years:>5}  "
                     f"{animal.status}")
    return "\n".join(lines)


def animal_card(animal):
    """Return a multi-line description of one animal."""
    human = animal.human_years()
    if human is None:
        human_text = "no rule for this species"
    else:
        human_text = f"{human} in human years"
    if animal.can_be_adopted():
        fee_text = f"${animal.fee()}"
    else:
        fee_text = "not available for adoption"
    if animal.good_with_kids:
        kids = "yes"
    else:
        kids = "no"
    lines = [
        f"{animal.name} ({animal.animal_id})",
        f"  {animal.species}, {animal.breed}, sex {animal.sex}",
        f"  Age: {animal.age_years} years ({human_text})",
        f"  Weight: {animal.weight_kg} kg, food {animal.daily_food()} g a day",
        f"  Status: {animal.status}, arrived {animal.arrived}",
        f"  Good with kids: {kids}",
        f"  Adoption fee: {fee_text}",
    ]
    if animal.notes:
        lines.append(f"  Notes: {animal.notes}")
    return "\n".join(lines)


def total(donations):
    result = 0
    for gift in donations:
        result += gift["amount"]
    return result


def total_by(donations, key):
    """Add up donations by "month" or by any column, such as "method"."""
    totals = {}
    for gift in donations:
        if key == "month":
            group = gift["date"][:7]
        else:
            group = gift[key]
        totals[group] = totals.get(group, 0) + gift["amount"]
    return totals


def average_gift(donations):
    if len(donations) == 0:
        return 0
    return total(donations) / len(donations)


def amount_of(pair):
    """The amount in a (donor, amount) pair: what top_donors() sorts by."""
    return pair[1]


def top_donors(donations, how_many=3):
    """Return [(donor, total), ...] for the biggest donors, biggest first."""
    pairs = list(total_by(donations, "donor").items())
    pairs.sort(key=amount_of, reverse=True)
    return pairs[:how_many]


def month_label(month):
    """Turn "2026-01" into "Jan 2026"."""
    year, number = month.split("-")
    return f"{MONTH_NAMES[int(number) - 1]} {year}"


def donations_summary(donations):
    """Return the donations summary as text."""
    lines = [f"Donations: {len(donations)} gifts, "
             f"total ${total(donations):,}, "
             f"average ${average_gift(donations):.2f}", "", "By month:"]
    for month, amount in sorted(total_by(donations, "month").items()):
        lines.append(f"  {month_label(month):<10}${amount:>7,}")
    lines.append("By method:")
    for method, amount in sorted(total_by(donations, "method").items()):
        lines.append(f"  {method:<10}${amount:>7,}")
    lines.append("Top donors:")
    for donor, amount in top_donors(donations):
        lines.append(f"  {donor:<26}${amount:>7,}")
    return "\n".join(lines)


def days_waiting(animal, today):
    return (today - date.fromisoformat(animal.arrived)).days


def shelter_report(shelter, today):
    """Return a full text report about the shelter on the date today."""
    lines = [f"{shelter.name}: shelter report for {today.isoformat()}",
             "=" * 60, "", "Animals by status:"]
    for status in ["Available", "Foster", "Medical hold", "Adopted"]:
        count = len(shelter.with_status(status))
        lines.append(f"  {status:<14}{count:>3}")

    lines += ["", "Spaces in use:"]
    for space, size in SPACES.items():
        used = 0
        for animal in shelter.animals:
            if SPACE_FOR[animal.species] == space and animal.status in ON_SITE:
                used += 1
        lines.append(f"  {space:<14}{used:>3} of {size}")

    on_site = [a for a in shelter.animals if a.status in ON_SITE]
    grams = 0
    for animal in on_site:
        grams += animal.daily_food()
    lines += ["", f"Food for the {len(on_site)} animals on site: "
                  f"{grams:,} g of dry food and pellets a day"]

    waiting = shelter.with_status("Available")   # already in arrival order
    lines += ["", "Waiting longest for a home:"]
    for animal in waiting[:5]:
        lines.append(f"  {animal.name:<10}{animal.species:<12}"
                     f"{days_waiting(animal, today):>4} days")

    lines += ["", donations_summary(shelter.donations)]
    return "\n".join(lines) + "\n"


def export_report(shelter, today, folder):
    """Write the shelter report into folder and return the file's path."""
    folder.mkdir(exist_ok=True)
    path = folder / f"shelter_report_{today.isoformat()}.txt"
    path.write_text(shelter_report(shelter, today), encoding="utf-8")
    return path
