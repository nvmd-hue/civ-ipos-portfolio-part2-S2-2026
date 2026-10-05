import questionary


def select(message: str, choices: list[str]) -> str:
    """Displays an interactive arrow-key selection menu."""
    return questionary.select(
        message,
        choices=choices,
        style=questionary.Style([
            ('pointer', 'fg: cyan bold'),
            ('highlighted', 'fg: cyan bold'),
        ])
    ).ask()
