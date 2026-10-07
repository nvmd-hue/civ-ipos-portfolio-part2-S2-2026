from src.task_manager import (add_task, delete_task, is_duplicate_title,
                              is_valid_date_format)
from src.file_handler import load_tasks
from src.menu_helper import select


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
    """Encapsulates the CLI prompt flow for deleting a task using
    menu_helper."""
    if not tasks:
        print("No Tasks found.")
        return

    choices = [(f"{task.title} | {task.description} | Due:"
                f" {task.due_date} | Status: {task.status}") for task in tasks]
    choices.append("Cancel")

    selected = select("Select task to delete:", choices)

    if selected == "Cancel" or not selected:
        return

    # Extract only title before first separator
    task_title = selected.split(" | ")[0]
    if delete_task(tasks, task_title):
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


def handle_change_task_status(tasks):
    """Encapsulates the CLI prompt flow for changing a task's status."""
    if not tasks:
        print("No tasks found.")
        return

    choices = [(f"{task.title} | {task.description} | Due:"
                f" {task.due_date} | Status: {task.status}") for task in tasks]
    choices.append("Cancel")

    selected = select("Select task to change status of:", choices)

    if selected == "Cancel" or not selected:
        return

    new_status = select(
        "Select new status:",
        ["Pending", "In Progress", "Completed", "Cancel"]
    )
    if new_status == "Cancel" or not new_status:
        return

    # Extract only title before first separator
    task_title = selected.split(" | ")[0]

    # Find and update the task status
    for task in tasks:
        if task.title == task_title:
            task.status = new_status
            print("Task status updated successfully.")
            return

    print("Task not found.")


def main():
    tasks = load_tasks()
    while True:
        choice = select(
            "Task Manager CLI", [
                "Add Task",
                "Delete Task",
                "List Tasks",
                "Change Task Status",
                "Exit"
            ]
        )

        if choice == "Add Task":
            handle_add_task_cli(tasks)
            print()
        elif choice == "Delete Task":
            handle_delete_task_cli(tasks)
            print()
        elif choice == "List Tasks":
            handle_list_task_cli(tasks)
            print()
        elif choice == "Change Task Status":
            handle_change_task_status(tasks)
            print()
        elif choice == "Exit" or choice is None:
            print("Exiting Task Manager.")
            break


if __name__ == "__main__":
    main()
