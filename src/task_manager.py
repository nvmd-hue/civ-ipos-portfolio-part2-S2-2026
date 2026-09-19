from src.task import Task
from src.file_handler import save_tasks
from datetime import datetime


def is_duplicate_title(tasks, title) -> bool:
    # Prevent duplicate tasks via case-insensitive check.
    return any(task.title.lower() == title.lower() for task in tasks)


def is_valid_date_format(due_date) -> datetime:
    # Validate correct date format. Returns ValueError if not valid.
    return datetime.strptime(due_date, "%d-%m-%Y")


def add_task(tasks, title, description, due_date):
    """
    Add a new task to the task list.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the new task.
        description (str): A brief description of the task.
        due_date (str): The due date of the task in 'DD-MM-YYYY' format.

    Returns:
        bool: True if the task is added successfully, False otherwise.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    tasks.append(Task(title, description, due_date))
    save_tasks(tasks)
    return True


def delete_task(tasks, title):
    """
    Delete a task from the task list based on its title.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the task to be deleted.

    Returns:
        bool: True if the task was found and deleted, False otherwise.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    for task in tasks:
        if task.title == title:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False


def filter_tasks_by_status(tasks, status):
    """
    Filter tasks by their status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str): The status to filter tasks by (e.g., "pending" or "completed").

    Returns:
        list: A list of Task objects that match the specified status.
    """
    return [task for task in tasks if task.status == status]
