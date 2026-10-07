# programs/ch15_weekly_report.py
"""Write the Sunny Paws weekly report from the shelter's data files.

Run it from the programs folder with the first day of the week, e.g.
    python3 ch15_weekly_report.py 2026-06-01
    python3 ch15_weekly_report.py 2026-06-01 --save
or with "last" for last week (Monday to Sunday), handy on a schedule:
    python3 ch15_weekly_report.py last --save
"""
import argparse
import csv
from datetime import date, timedelta
from pathlib import Path

DATA = Path("../data")
OUTPUT = Path("output")


def read_csv(path):
    """Return the rows of a CSV file as a list of dictionaries."""
    with open(path, encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def in_period(text, start, end):
    """True if a date written like "2026-06-03" is from start to end."""
    if text == "":
        return False
    return start <= date.fromisoformat(text) <= end


def build_report(start, days):
    """Return the lines of the report for the given period."""
    end = start + timedelta(days=days - 1)
    donations = [row for row in read_csv(DATA / "donations.csv")
                 if in_period(row["date"], start, end)]
    animals = read_csv(DATA / "animals.csv")
    arrived = [row for row in animals if in_period(row["arrived"], start, end)]
    adopted = [row for row in animals
               if in_period(row["adopted_on"], start, end)]
    visits = 0
    with open(DATA / "visitor_log.txt", encoding="utf-8") as file:
        for line in file:
            if line.strip() and in_period(line.split()[0], start, end):
                visits += 1

    first_day = start.strftime("%a %d %b %Y")
    last_day = end.strftime("%a %d %b %Y")
    lines = ["Sunny Paws weekly report", f"{first_day} to {last_day}",
             "=" * 40, ""]
    total = 0
    biggest = None
    for row in donations:
        amount = int(row["amount"])
        total += amount
        if biggest is None or amount > int(biggest["amount"]):
            biggest = row
    lines.append(f"Donations: {len(donations)}, ${total:,} in total")
    if biggest is not None:
        lines.append(f"  Biggest: ${biggest['amount']} from "
                     f"{biggest['donor']} on {biggest['date']}")
    lines.append("")
    lines.append(f"Arrived: {len(arrived)}")
    for row in arrived:
        lines.append(f"  {row['id']}  {row['name']} ({row['species']})")
    lines.append(f"Adopted: {len(adopted)}")
    for row in adopted:
        lines.append(f"  {row['id']}  {row['name']} ({row['species']})")
    lines.append("")
    lines.append(f"Visits in the visitor log: {visits}")
    return lines


def main():
    parser = argparse.ArgumentParser(
        description="Print the Sunny Paws weekly report.")
    parser.add_argument("start",
                        help='first day, like 2026-06-01, or "last" for '
                             "last week")
    parser.add_argument("--days", type=int, default=7,
                        help="how many days to cover (default: 7)")
    parser.add_argument("--save", action="store_true",
                        help="also save the report in the output folder")
    args = parser.parse_args()

    if args.start == "last":
        today = date.today()
        start = today - timedelta(days=today.weekday() + 7)
    else:
        try:
            start = date.fromisoformat(args.start)
        except ValueError:
            parser.error(f"'{args.start}' is not a date like 2026-06-01")

    lines = build_report(start, args.days)
    for line in lines:
        print(line)
    if args.save:
        OUTPUT.mkdir(exist_ok=True)
        report_file = OUTPUT / f"weekly_report_{start}.txt"
        report_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"\nSaved to {report_file}")


if __name__ == "__main__":
    main()
