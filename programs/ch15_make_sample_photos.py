# programs/ch15_make_sample_photos.py
"""Create a sample folder of pretend pet photos to practice on.

Run this from the programs folder. It creates output/pet_photos/ with a few
small files. It never touches any other folder. To start over, delete the
output/pet_photos folder yourself and run this again.
"""
from pathlib import Path

SAMPLE_FOLDER = Path("output/pet_photos")
SAMPLE_FILES = [
    "IMG_20260412_093000.jpg",
    "IMG_20260412_093512.JPG",
    "IMG_20260503_141020.jpeg",
    "IMG_20260521_160245.jpg",
    "IMG_20260603_101500.jpg",
    "Peanut at the park.jpg",
    "Truffle SLEEPING.PNG",
    "Kiwi bath time.MOV",
    "adoption form Gus.pdf",
    "vet notes Mochi.txt",
]


def main():
    if SAMPLE_FOLDER.exists():
        print(f"{SAMPLE_FOLDER} already exists, so nothing was changed.")
        print("Delete that folder yourself if you want a fresh copy.")
        return
    SAMPLE_FOLDER.mkdir(parents=True)
    for name in SAMPLE_FILES:
        path = SAMPLE_FOLDER / name
        path.write_text(f"Pretend file: {name}\n", encoding="utf-8")
    print(f"Created {len(SAMPLE_FILES)} sample files in {SAMPLE_FOLDER}")


if __name__ == "__main__":
    main()
