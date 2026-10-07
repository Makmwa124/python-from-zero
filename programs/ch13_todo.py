# programs/ch13_todo.py
"""A Sunny Paws to-do list that remembers its tasks between runs.

Run this from the programs folder. The tasks are saved in output/todo.json.
"""
import json
from pathlib import Path

TODO_FILE = Path("output/todo.json")


def load_tasks():
    """Return the saved list of tasks, or an empty list if there is none."""
    try:
        with open(TODO_FILE, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved list yet, so starting a new one.")
        return []


def save_tasks(tasks):
    """Save the list of tasks as JSON."""
    TODO_FILE.parent.mkdir(exist_ok=True)
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def main():
    tasks = load_tasks()
    print(f"You have {len(tasks)} task(s) on the list.")
    for number, task in enumerate(tasks, start=1):
        print(f"  {number}. {task}")
    while True:
        new_task = input("New task (press Enter to finish): ").strip()
        if new_task == "":
            break
        tasks.append(new_task)
    save_tasks(tasks)
    print(f"Saved {len(tasks)} task(s) to {TODO_FILE}")


if __name__ == "__main__":
    main()
