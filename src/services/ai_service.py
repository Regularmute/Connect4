import random

class connect4AI:
    """Artificial intelligence for the game."""

    def __init__(self, game_service):
        self.game_service = game_service

    def choose_column(self):
        """Chooses a random column to drop a piece in."""
        column = random.randint(0, 6)
        while self.game_service.game_grid[0][column] != ".":
            column = random.randint(0, 6)
        return column
