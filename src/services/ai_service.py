import random

class Connect4AI:
    """Artificial intelligence for the game.

    Attributes:
        game_service(GameService): The game logic with the game's information.
    """

    def __init__(self, game_service):
        self.game_service = game_service

    def choose_column(self):
        """Chooses a random column to drop a piece in.

        Returns:
            column(int): The column number to drop the piece in.
        """
        column = random.randint(0, 6)
        while self.game_service.game_grid[0][column] != ".":
            column = random.randint(0, 6)
        return column
