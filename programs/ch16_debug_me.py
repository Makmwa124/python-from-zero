# programs/ch16_debug_me.py
"""A tiny copy of the buggy monthly total, for practising with pdb."""

GIFTS = [
    {"date": "2026-01-03", "donor": "Chris Doyle", "amount": 50},
    {"date": "2026-01-10", "donor": "Maple Falls Bakery", "amount": 100},
    {"date": "2026-02-14", "donor": "Grace Kim", "amount": 25},
]


def total_by_month(donations):
    totals = {}
    for gift in donations:
        month = gift["date"][:7]
        breakpoint()
        totals[month] = gift["amount"]
    return totals


print(total_by_month(GIFTS))
