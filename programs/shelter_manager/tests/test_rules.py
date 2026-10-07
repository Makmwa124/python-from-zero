# programs/shelter_manager/tests/test_rules.py
"""Tests for rules.py. Run from the shelter_manager folder:
python3 -m pytest
"""
from datetime import date

import pytest

from rules import adoption_fee, food_grams, human_years, is_adoption_day


def test_human_years_follow_the_poster():
    assert human_years("Dog", 3) == 29
    assert human_years("Cat", 3) == 28
    assert human_years("Dog", 0.5) == 7.5


def test_no_human_years_rule_for_rabbits():
    with pytest.raises(ValueError):
        human_years("Rabbit", 2)


def test_fees_and_senior_discount():
    assert adoption_fee("Dog", 3, "Available") == 150
    assert adoption_fee("Cat", 8, "Foster") == 45
    assert adoption_fee("Rabbit", 9, "Available") == 45


def test_fees_waived_on_adoption_day():
    assert adoption_fee("Dog", 3, "Available", adoption_day=True) == 0


def test_medical_hold_has_no_fee():
    with pytest.raises(ValueError):
        adoption_fee("Cat", 5, "Medical hold")


def test_food():
    assert food_grams("Dog", 4.5, 28.6) == 429
    assert food_grams("Cat", 0.6, 1.7) == 80
    assert food_grams("Guinea pig", 1, 1.2) == 40


def test_adoption_day_is_first_saturday_of_october():
    assert is_adoption_day(date(2026, 10, 3))        # a Saturday
    assert not is_adoption_day(date(2026, 10, 10))   # second Saturday
    assert not is_adoption_day(date(2026, 10, 6))    # a Tuesday
    assert not is_adoption_day(date(2026, 9, 5))     # September
