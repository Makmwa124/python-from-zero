# programs/ch16_bug_hunt/test_donations_report.py
"""Tests for donations_report.py, written before fixing anything."""
from donations_report import average_gift, total, total_by_month

GIFTS = [
    {"date": "2026-01-03", "donor": "Chris Doyle", "amount": 50},
    {"date": "2026-01-10", "donor": "Maple Falls Bakery", "amount": 100},
    {"date": "2026-02-14", "donor": "Grace Kim", "amount": 25},
]


def test_total():
    assert total(GIFTS) == 175


def test_two_gifts_in_january_are_added():
    monthly = total_by_month(GIFTS)
    assert monthly["2026-01"] == 150


def test_months_add_up_to_the_total():
    monthly = total_by_month(GIFTS)
    months_added = sum(monthly.values())
    assert months_added == 175


def test_average_gift():
    assert average_gift(GIFTS) == 175 / 3


def test_no_gifts_at_all():
    assert total([]) == 0
    assert total_by_month([]) == {}
    assert average_gift([]) == 0
