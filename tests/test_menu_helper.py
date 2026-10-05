import unittest
from unittest.mock import patch
from src.menu_helper import select


class TestMenuHelper(unittest.TestCase):

    @patch('menu_helper.questionary.select')
    def test_select_returns_choice(self, mock_questionary_select):
        mock_ask = mock_questionary_select.return_value.ask
        mock_ask.return_value = "Add Task"

        result = select("Choose an option:", ["Add Task", "Exit"])

        mock_questionary_select.assert_called_once_with(
            "Choose an option:",
            choices=["Add Task", "Exit"],
            style=unittest.mock.ANY
        )
        mock_ask.assert_called_once()
        self.assertEqual(result, "Add Task")

    if __name__ == "__main__":
        unittest.main()
