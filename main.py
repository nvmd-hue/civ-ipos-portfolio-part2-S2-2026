from src.task_manager import (add_task, delete_task, is_duplicate_title,
                              is_valid_date_format)
from src.file_handler import load_tasks


def handle_add_task_cli(tasks):
    """Encapsulates the CLI prompt flow and validation for adding a task."""
    title = input("Title: ")
    if is_duplicate_title(tasks, title):
        print("Error: A task with this title already exists.")
        return

    description = input("Description: ")
    due_date = input("Due Date (DD-MM-YYYY): ")

    try:
        is_valid_date_format(due_date)
    except ValueError:
        print("Error: Invalid date format. Use DD-MM-YYYY.")
        return

    add_task(tasks, title, description, due_date)


def handle_delete_task_cli(tasks):
    """Encapsulates the CLI prompt flow for deleting a task."""
    title = input("Title of the task to delete: ")
    if delete_task(tasks, title):
        print("Task deleted successfully.")
    else:
        print("Task not found.")


def handle_list_task_cli(tasks):
    """Encapsulates the CLI prompt flow for listing tasks."""
    # Check if task list is empty. Empty lists eval to bool False.
    if not tasks:
        print("No tasks found.")
        return
    # Task list is not empty so print contents to console
    for task in tasks:
        print(
            f"{task.title} | {task.description} | "
            f"Due: {task.due_date} | Status: {task.status}"
        )


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            handle_add_task_cli(tasks)
        elif choice == "2":
            handle_delete_task_cli(tasks)
        elif choice == "3":
            handle_list_task_cli(tasks)
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
