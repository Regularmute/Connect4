"""Handles the impartial game logic."""

class GameService:
    """Represents the game logic in charge of tracking the current game state.
    Attributes:
            game_grid(list): A 2D list of 6 rows and 7 columns.
            running(bool): True if the game is running,
                False if the game is over.
    """
    def __init__(self):
        """Initializes the game grid and sets the game to running.

        The game grid is a 2D list of 6 rows and 7 columns. Each empty tile is
        represented by a character:
            '.' = empty tile
            'X' = player piece (human)
            'O' = computer piece
        """
        self.game_grid = [['.' for _ in range(7)] for _ in range(6)]
        self.running = True

    def update_grid(self, grid, column, player):
        """Updates the grid with a piece dropped by a player.

        Args:
            grid(list): The game grid to update.
            column(int, 0-6): The column number to drop the piece in.
            player(bool): True if the piece is dropped by the player,
                False if dropped by the computer.
        """
        column = int(column)

        if player:
            piece = "X"
        else:
            piece = "O"

        for row in range(5, -1, -1):
            if self.game_grid[row][column] == ".":
                self.game_grid[row][column] = piece
                piece_row = row
                piece_column = column
                if self.check_win_including_piece(piece_row, piece_column):
                    if player:
                        print("You win!")
                    else:
                        print("You lose!")
                    self.running = False
                break

    def check_win_including_piece(self, piece_row=5, piece_column=0):
        """Checks if the game has been won with a piece.

        Args:
            piece_row(int): The row number of the last piece dropped.
            piece_column(int): The column number of the last piece dropped.

        Returns:
            True if the game has been won, False if not.
        """

        new_piece = self.game_grid[piece_row][piece_column]

        if new_piece == ".":
            return False

        # Check vertical connections
        if piece_row < 3:
            if all(self.game_grid[piece_row+i][piece_column] == new_piece for i in range(4)):
                return True

        # Check horizontal connections
        for column in range(max(0, piece_column-3), min(3, piece_column+1)):
            if all(
                self.game_grid[piece_row][column+i]
                == new_piece for i in range(4)
                ):
                return True

        # Check falling diagonal connections
        for row in range(max(0, piece_row-3), min(3, piece_row+1)):
            for column in range(
                max(0,piece_column-3), min(3, piece_column+1)
                ):
                if all(
                    self.game_grid[row+i][column+i]
                    == new_piece for i in range(4)
                    ):
                    return True

        # Check rising diagonal connections
        for row in range(min(5, piece_row+3), piece_row-1, -1):
            for column in range(
                max(0,piece_column-3), min(3, piece_column+1)
                ):
                if all(
                    self.game_grid[row-i][column+i]
                    == new_piece for i in range(4)):
                    return True
        return False
