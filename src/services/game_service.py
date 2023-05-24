class GameService:
    def __init__(self):
        """Initializes the game grid and sets the game to running.

        The game grid is a 2D list of 6 rows and 7 columns. Each empty tile is
        represented by a character:
            '.' = empty tile
            'X' = player piece (human)
            'O' = computer piece

        Attributes:
            game_grid(list): A 2D list of 6 rows and 7 columns.
            running(bool): True if the game is running, False if the game is over.
        """
        self.game_grid = [['.' for _ in range(7)] for _ in range(6)]  
        self.running = True 

    def print_grid(self):
        for row in self.game_grid:
            print(row)
    
    def update_grid(self, column, player):
        """Updates the grid with a piece dropped by a player.

        Args:
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
                if self.check_win(piece_row, piece_column):
                    self.print_grid()
                    if player:
                        print("You win!")
                    else:
                        print("You lose!")
                    self.running = False
                break
            else:
                continue


    def check_win(self, piece_row=5, piece_column=0):
        """Checks if the game has been won around a piece.

        Args:
            piece_row(int): The row number of the last piece dropped.
            piece_column(int): The column number of the last piece dropped.

        Returns:
            True if the game has been won, False if not.
        """
        for row in range(piece_row-3, piece_row+4):
            if row < 0 or row > 5:
                continue
            for column in range(piece_column-3, piece_column+4):
                if column < 0 or column > 6:
                    continue
                if self.game_grid[row][column] != ".":
                    try:
                        if (self.game_grid[row][column]
                            == self.game_grid[row][column+1]
                            == self.game_grid[row][column+2]
                            == self.game_grid[row][column+3]
                        ):
                            return True
                    except IndexError:
                        pass
                    try:
                        if (self.game_grid[row][column]
                            == self.game_grid[row+1][column]
                            == self.game_grid[row+2][column]
                            == self.game_grid[row+3][column]
                        ):
                            return True
                    except IndexError:
                        pass
                    try:
                        if (self.game_grid[row][column]
                            == self.game_grid[row+1][column+1]
                            == self.game_grid[row+2][column+2]
                            == self.game_grid[row+3][column+3]
                        ):
                            return True
                    except IndexError:
                        pass
                    try:
                        if (self.game_grid[row][column]
                            == self.game_grid[row+1][column-1]
                            == self.game_grid[row+2][column-2]
                            == self.game_grid[row+3][column-3]
                        ):
                            return True
                    except IndexError:
                        continue
        return False

game_service = GameService()