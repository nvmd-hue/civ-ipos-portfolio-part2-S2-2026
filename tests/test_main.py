from unittest.mock import patch, MagicMock
import unittest
import main
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))


class TestCLIHandlers(unittest.TestCase):
    """Unittest mocking objects and inputs to validate the CLI handlers
    control flow."""

    # Tests for main.handle_add_task_cli()
    @patch('main.add_task')
    @patch('main.is_valid_date_format')
    @patch('main.is_duplicate_title', return_value=False)
    @patch(
        'builtins.input', side_effect=['Task 1', 'Description', '10-10-2026']
    )
    def test_handle_add_task_cli_pass(
        self, mock_input, mock_is_duplicate, mock_is_valid, mock_add
    ):
        tasks = []
        main.handle_add_task_cli(tasks)

        mock_is_duplicate.assert_called_once_with(tasks, 'Task 1')
        mock_is_valid.assert_called_once_with('10-10-2026')
        mock_add.assert_called_once_with(
            tasks, 'Task 1', 'Description', '10-10-2026'
        )

    @patch('main.is_duplicate_title', return_value=True)
    @patch('builtins.print')
    @patch('builtins.input', return_value='Existing Task')
    def test_handle_add_task_cli_duplicate(
        self, mock_input, mock_print, mock_is_duplicate
    ):
        tasks = []
        main.handle_add_task_cli(tasks)

        mock_is_duplicate.assert_called_once_with(tasks, 'Existing Task')
        mock_print.assert_called_once_with(
            "Error: A task with this title already exists."
        )

    @patch('main.is_valid_date_format', side_effect=ValueError)
    @patch('main.is_duplicate_title', return_value=False)
    @patch('builtins.print')
    @patch(
        'builtins.input', side_effect=['Task 1', 'Description', 'invalid_date']
    )
    def test_handle_add_task_cli_invalid_date(
        self, mock_input, mock_print, mock_is_duplicate, mock_is_valid
    ):
        tasks = []
        main.handle_add_task_cli(tasks)

        mock_is_valid.assert_called_once_with('invalid_date')
        mock_print.assert_called_once_with(
            "Error: Invalid date format. Use DD-MM-YYYY."
        )

    # Tests for main.handle_delete_task_cli()
    @patch('main.delete_task', return_value=False)
    @patch('builtins.print')
    @patch('builtins.input', return_value='Task 1')
    def test_handle_delete_task_cli_fail(
        self, mock_input, mock_print,
        mock_delete
    ):
        tasks = []
        main.handle_delete_task_cli(tasks)

        mock_delete.assert_called_once_with(tasks, 'Task 1')
        mock_print.assert_called_once_with("Task not found.")

    @patch('main.delete_task', return_value=True)
    @patch('builtins.print')
    @patch('builtins.input', return_value='Task 1')
    def test_handle_delete_task_cli_pass(
        self, mock_input, mock_print, mock_delete
    ):
        tasks = []
        main.handle_delete_task_cli(tasks)

        mock_delete.assert_called_once_with(tasks, 'Task 1')
        mock_print.assert_called_once_with("Task deleted successfully.")

    # Tests for main.handle_list_task_cli()
    @patch('builtins.print')
    def test_handle_list_task_cli_fail(self, mock_print):
        # Empty task list will eval as False bool.
        tasks = []
        main.handle_list_task_cli(tasks)

        mock_print.assert_called_once_with("No tasks found.")

    @patch('builtins.print')
    def test_handle_list_task_cli_pass(self, mock_print):
        mock_task = MagicMock(
            title='Task 1',
            description='Do things',
            due_date='10-10-2026',
            status='Pending'
        )
        tasks = [mock_task]

        main.handle_list_task_cli(tasks)

        mock_print.assert_called_once_with(
            "Task 1 | Do things | Due: 10-10-2026 | Status: Pending"
        )
