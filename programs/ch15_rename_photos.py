# programs/ch15_rename_photos.py
"""Tidy up photo file names: dates first, lowercase, hyphens, .jpg.

Safe by default: without --apply it only prints what it would do.
Run it from the programs folder, for example:
    python3 ch15_rename_photos.py output/pet_photos
    python3 ch15_rename_photos.py output/pet_photos --apply
"""
import argparse
from pathlib import Path

PHOTO_TYPES = [".jpg", ".jpeg", ".png"]


def tidy_name(path):
    """Return the tidy file name for one photo."""
    stem = path.stem.lower().replace(" ", "-")
    if stem.startswith("img_") and len(stem) == 19:
        # A camera name like img_20260412_093000 becomes 2026-04-12_093000
        day = stem[4:12]
        stem = f"{day[:4]}-{day[4:6]}-{day[6:]}_{stem[13:]}"
    suffix = path.suffix.lower()
    if suffix == ".jpeg":
        suffix = ".jpg"
    return stem + suffix


def plan_renames(folder):
    """Return a list of (old_path, new_path) pairs for the photos."""
    plan = []
    for path in sorted(folder.iterdir()):
        if path.is_file() and path.suffix.lower() in PHOTO_TYPES:
            new_path = path.with_name(tidy_name(path))
            if new_path != path:
                plan.append((path, new_path))
    return plan


def main():
    parser = argparse.ArgumentParser(
        description="Tidy up the names of photo files in a folder.")
    parser.add_argument("folder", help="the folder that holds the photos")
    parser.add_argument("--apply", action="store_true",
                        help="really rename the files (default: dry run)")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"There is no folder called {folder}")
        return

    plan = plan_renames(folder)
    if not plan:
        print("Nothing to rename: every photo name is already tidy.")
        return
    for old_path, new_path in plan:
        if new_path.exists():
            print(f"SKIP   {old_path.name} ({new_path.name} already exists)")
        elif args.apply:
            old_path.rename(new_path)
            print(f"RENAMED  {old_path.name}  ->  {new_path.name}")
        else:
            print(f"WOULD RENAME  {old_path.name}  ->  {new_path.name}")
    if not args.apply:
        print("This was a dry run. Add --apply to rename the files.")


if __name__ == "__main__":
    main()
