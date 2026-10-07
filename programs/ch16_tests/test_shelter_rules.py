# programs/ch16_tests/test_shelter_rules.py
"""Tests for shelter_rules.py. Run them with: python3 -m pytest"""
import pytest

from shelter_rules import adoption_fee, food_grams, human_years


# --- human_years -------------------------------------------------------

def test_three_year_old_dog():
    assert human_years("Dog", 3) == 29


def test_three_year_old_cat():
    assert human_years("Cat", 3) == 28


def test_puppy_scales_the_first_year():
    assert human_years("Dog", 0.5) == 7.5


def test_newborn_is_zero():
    assert human_years("Cat", 0) == 0


def test_human_years_rejects_rabbits():
    with pytest.raises(ValueError):
        human_years("Rabbit", 2)


def test_human_years_rejects_negative_age():
    with pytest.raises(ValueError):
        human_years("Dog", -1)


def test_age_typed_as_text_is_an_error():
    with pytest.raises(TypeError):
        human_years("Dog", "3")


# --- adoption_fee ------------------------------------------------------

def test_basic_fees():
    assert adoption_fee("Dog", 3, "Available") == 150
    assert adoption_fee("Cat", 3, "Available") == 90
    assert adoption_fee("Rabbit", 3, "Available") == 45
    assert adoption_fee("Guinea pig", 3, "Available") == 25


def test_senior_dog_pays_half():
    assert adoption_fee("Dog", 10, "Available") == 75


def test_exactly_eight_counts_as_senior():
    assert adoption_fee("Cat", 8, "Available") == 45


def test_old_rabbit_pays_full_fee():
    assert adoption_fee("Rabbit", 9, "Available") == 45


def test_species_typed_in_lowercase():
    assert adoption_fee("dog ", 3, "Foster") == 150


def test_medical_hold_cannot_be_adopted():
    with pytest.raises(ValueError):
        adoption_fee("Dog", 3, "Medical hold")


# --- food_grams --------------------------------------------------------

def test_dog_food_uses_weight():
    assert food_grams("Dog", 4.5, 28.6) == 429


def test_kitten_and_adult_cat():
    assert food_grams("Cat", 0.6, 1.7) == 80
    assert food_grams("Cat", 3, 4.0) == 60


def test_small_animals():
    assert food_grams("Rabbit", 2, 1.4) == 80
    assert food_grams("Guinea pig", 1, 1.2) == 40
