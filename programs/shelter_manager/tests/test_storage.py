# programs/shelter_manager/tests/test_storage.py
"""Tests for storage.py: reading the CSV files, saving and loading JSON."""
from storage import (DATA, load_animals_csv, load_donations_csv, load_shelter,
                     save_shelter, start_shelter)


def test_csv_import_converts_types():
    animals = load_animals_csv(DATA / "animals.csv")
    assert len(animals) == 48
    peanut = animals[0]
    assert peanut.name == "Peanut"
    assert peanut.age_years == 4.5               # a number, not "4.5"
    assert peanut.good_with_kids is False        # a bool, not "no"


def test_donations_import():
    donations = load_donations_csv(DATA / "donations.csv")
    assert len(donations) == 130
    assert donations[0]["amount"] == 150


def test_save_then_load_gives_the_same_shelter(tmp_path):
    shelter, message = start_shelter(tmp_path / "nothing_saved_yet.json")
    shelter.find("SP-010").status = "Adopted"
    save_file = tmp_path / "shelter_data.json"
    save_shelter(shelter, save_file)
    again = load_shelter(save_file)
    assert len(again.animals) == 48
    assert again.find("SP-010").status == "Adopted"
    assert again.find("SP-001").weight_kg == 28.6
    assert again.donations == shelter.donations


def test_start_prefers_the_saved_file(tmp_path):
    save_file = tmp_path / "shelter_data.json"
    shelter, message = start_shelter(save_file)
    assert "CSV" in message
    save_shelter(shelter, save_file)
    shelter, message = start_shelter(save_file)
    assert "shelter_data.json" in message
