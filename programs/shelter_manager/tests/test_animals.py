# programs/shelter_manager/tests/test_animals.py
"""Tests for the Animal and Shelter classes."""
from datetime import date

import pytest

from animals import Animal, Shelter


def make_shelter():
    """A tiny shelter with three animals, fresh for each test."""
    shelter = Shelter()
    shelter.add(Animal("SP-001", "Peanut", "Dog", "Labrador mix", "M",
                       4.5, 28.6, "2026-01-07"))
    shelter.add(Animal("SP-002", "Truffle", "Cat", "Tuxedo", "F", 1, 3.9,
                       "2026-01-07", status="Medical hold"))
    shelter.add(Animal("SP-009", "Poppy", "Dog", "Boxer mix", "F", 10,
                       30.7, "2026-02-02", status="Foster",
                       notes="Loves belly rubs"))
    return shelter


def test_find_ignores_case_and_spaces():
    shelter = make_shelter()
    assert shelter.find(" sp-002 ").name == "Truffle"
    assert shelter.find("SP-999") is None


def test_search_looks_in_names_breeds_and_notes():
    shelter = make_shelter()
    assert [a.name for a in shelter.search("BOXER")] == ["Poppy"]
    assert [a.name for a in shelter.search("belly")] == ["Poppy"]
    assert shelter.search("hamster") == []


def test_next_id_follows_the_highest():
    assert make_shelter().next_id() == "SP-010"


def test_spaces_free_counts_only_animals_on_site():
    shelter = make_shelter()
    assert shelter.spaces_free("Dog") == 19    # Poppy is in foster care
    assert shelter.spaces_free("Cat") == 15


def test_adopt_records_status_date_and_fee():
    shelter = make_shelter()
    fee = shelter.adopt("SP-009", date(2026, 10, 6))
    poppy = shelter.find("SP-009")
    assert fee == 75                           # senior dog: half price
    assert poppy.status == "Adopted"
    assert poppy.adopted_on == "2026-10-06"


def test_adopt_on_adoption_day_is_free():
    shelter = make_shelter()
    assert shelter.adopt("SP-001", date(2026, 10, 3)) == 0


def test_cannot_adopt_twice_or_on_medical_hold():
    shelter = make_shelter()
    shelter.adopt("SP-001", date(2026, 10, 6))
    with pytest.raises(ValueError):
        shelter.adopt("SP-001", date(2026, 10, 6))
    with pytest.raises(ValueError):
        shelter.adopt("SP-002", date(2026, 10, 6))


def test_animal_without_human_years_rule():
    hazel = Animal("SP-011", "Hazel", "Rabbit", "Rex", "M", 3, 2.5,
                   "2026-02-07")
    assert hazel.human_years() is None
    assert hazel.daily_food() == 80
