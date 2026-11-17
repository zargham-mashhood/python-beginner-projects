"""Simple to-do list app (command line).

Lets you add tasks, list them, mark them done and delete them.
Tasks are saved to a small JSON file (tasks.json) in the same folder,
so they are still there the next time you run the app.

Run:  python3 todo.py
"""

import json
import os

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    """Read the saved tasks from disk, or return an empty list."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    """Write the task list to disk."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    """Print the task list with numbers and done/pending marks."""
    if not tasks:
        print("No tasks yet. Add one with option 1.")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        mark = "[x]" if task["done"] else "[ ]"
        print(f"  {i}. {mark} {task['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Mark a task done")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Task: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print(f"Added: {title}")
            else:
                print("Task text cannot be empty.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Task number to mark done: "))
                tasks[num - 1]["done"] = True
                save_tasks(tasks)
                print("Marked as done.")
            except (ValueError, IndexError):
                print("Please enter a valid task number.")

        elif choice == "4":
            show_tasks(tasks)
            try:
                num = int(input("Task number to delete: "))
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Deleted: {removed['title']}")
            except (ValueError, IndexError):
                print("Please enter a valid task number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
