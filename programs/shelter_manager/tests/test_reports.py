# programs/shelter_manager/tests/test_reports.py
"""Tests for reports.py, using small hand-made donations."""
from reports import (average_gift, month_label, top_donors, total,
                     total_by)

GIFTS = [
    {"date": "2026-01-03", "donor": "Chris Doyle", "amount": 50,
     "method": "cash"},
    {"date": "2026-01-10", "donor": "Maple Falls Bakery", "amount": 100,
     "method": "card"},
    {"date": "2026-02-14", "donor": "Chris Doyle", "amount": 25,
     "method": "cash"},
]


def test_totals():
    assert total(GIFTS) == 175
    assert total_by(GIFTS, "month") == {"2026-01": 150, "2026-02": 25}
    assert total_by(GIFTS, "method") == {"cash": 75, "card": 100}


def test_top_donors_adds_up_each_donor():
    assert top_donors(GIFTS, 2) == [("Maple Falls Bakery", 100),
                                    ("Chris Doyle", 75)]


def test_no_donations():
    assert total([]) == 0
    assert average_gift([]) == 0
    assert top_donors([]) == []


def test_month_label():
    assert month_label("2026-01") == "Jan 2026"
    assert month_label("2026-12") == "Dec 2026"
