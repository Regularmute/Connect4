class GameUI:
    """User interface for the game."""
    def __init__(self, game_service):
        self.game_service = game_service

    def print_grid(self):
        """Prints the game grid stored in the game logic to the console."""
        for row in self.game_service.game_grid:
            print(row)

    def get_column_from_player(self):
        """Gets the column number from the player."""
        while True:
            try:
                column = int(input("Enter a column number (1-7): ")) - 1
                if column < 0 or column > 6:
                    raise ValueError
                if self.game_service.game_grid[0][column] != ".":
                    print("Column is full, please choose another.")
                    continue
                return column
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")
                continue

