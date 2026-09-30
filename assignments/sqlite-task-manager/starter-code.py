import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name("tasks.db")


def initialize_database():
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


def add_task(title):
    raise NotImplementedError("Save the task and return its new ID")


def list_tasks():
    raise NotImplementedError("Return all tasks ordered by ID")


def mark_task_complete(task_id):
    raise NotImplementedError("Mark the matching task complete")


def main():
    initialize_database()

    while True:
        print("\n1. Add task\n2. List tasks\n3. Complete task\n4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            if title:
                task_id = add_task(title)
                print(f"Added task {task_id}.")
            else:
                print("Task title cannot be empty.")
        elif choice == "2":
            tasks = list_tasks()
            if tasks:
                for task_id, title, completed in tasks:
                    status = "complete" if completed else "incomplete"
                    print(f"{task_id}. {title} [{status}]")
            else:
                print("No tasks yet.")
        elif choice == "3":
            try:
                task_id = int(input("Task ID to complete: "))
            except ValueError:
                print("Enter a valid integer ID.")
                continue

            if mark_task_complete(task_id):
                print("Task marked complete.")
            else:
                print("Task ID not found.")
        elif choice == "4":
            break
        else:
            print("Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()