class GameUI:
    """User interface for the game."""
    def __init__(self, game_ai):
        """
        args: game_ai(GameAI): The game module in charge of tracking game state
            and running the minimax algorithm for optimal computer moves.
        """
        self.game_ai = game_ai

    def print_grid(self):
        """Prints the game grid stored in the game logic to the console."""
        for row in self.game_ai.game_grid:
            print(row)

    def get_column_from_player(self):
        """Gets the column number from the player.

        Handles invalid inputs such as non-integers, non-existing columns or
        columns without free spaces.

        Returns:
            column(int): The index of the column where the player drops a piece.
        """
        while True:
            try:
                column = int(input("Enter a column number (1-7): ")) - 1
                if column < 0 or column > 6:
                    raise ValueError
                if self.game_ai.game_grid[0][column] != 0:
                    print("Column is full, please choose another.")
                    continue
                return column
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")
                continue
