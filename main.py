from src.task_manager import add_task, delete_task, list_tasks, is_duplicate_title
from src.file_handler import load_tasks
from task_manager import is_valid_date_format


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
            # Validate no task duplication
            title = input("Title: ")
            if is_duplicate_title(tasks, title):
                print("Error: A task with this title already exists.")
                continue

            description = input("Description: ")

            # Validate correct date format
            due_date = input("Due Date (DD-MM-YYYY): ")
            try:
                is_valid_date_format(due_date)
            except ValueError:
                print("Error: Invalid date format. Use DD-MM-YYYY.")
                continue

            add_task(tasks, title, description, due_date)

        elif choice == "2":
            title = input("Title of the task to delete: ")
            if delete_task(tasks, title):
                print("Task deleted successfully.")
            else:
                print("Task not found.")
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
