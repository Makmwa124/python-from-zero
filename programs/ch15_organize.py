# programs/ch15_organize.py
"""Move the files in a folder into subfolders by type.

Safe by default: without --apply it only prints what it would do.
Run it from the programs folder, for example:
    python3 ch15_organize.py output/pet_photos --apply
"""
import argparse
import shutil
from pathlib import Path

FOLDER_FOR_TYPE = {
    ".jpg": "photos", ".jpeg": "photos", ".png": "photos",
    ".mov": "videos", ".mp4": "videos",
    ".pdf": "documents", ".txt": "documents", ".docx": "documents",
}


def main():
    parser = argparse.ArgumentParser(
        description="Sort the files in a folder into subfolders by type.")
    parser.add_argument("folder", help="the folder to organize")
    parser.add_argument("--apply", action="store_true",
                        help="really move the files (default: dry run)")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"There is no folder called {folder}")
        return

    moved = 0
    for path in sorted(folder.iterdir()):
        if not path.is_file():
            continue
        subfolder_name = FOLDER_FOR_TYPE.get(path.suffix.lower(), "other")
        target_folder = folder / subfolder_name
        target = target_folder / path.name
        if target.exists():
            print(f"SKIP   {path.name} (already in {subfolder_name}/)")
            continue
        if args.apply:
            target_folder.mkdir(exist_ok=True)
            shutil.move(path, target)
            print(f"MOVED       {path.name}  ->  {subfolder_name}/")
        else:
            print(f"WOULD MOVE  {path.name}  ->  {subfolder_name}/")
        moved += 1

    if args.apply:
        print(f"Moved {moved} file(s).")
    else:
        print(f"Dry run: {moved} file(s) would move. Add --apply to do it.")


if __name__ == "__main__":
    main()
