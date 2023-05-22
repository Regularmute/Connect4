class Connect4Game:
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
                break
            else:
                continue

    def ask_for_input(self):
        """Prompts the user for a column number to drop a piece in.

        Calls update_grid() if the input is valid.
        Exceptions:
            ValueError: If the input is not an integer.
            IndexError: If the input is not between 1-7.
        """
        print("Please enter a column number (1-7): ")
        try:
            column = int(input()) - 1
            if self.game_grid[0][column] != ".":
                print("Column is full, please choose another.")
            elif column == -1:
                self.running = False
            else:
                self.update_grid(column, True)
        except ValueError:
            print("Invalid column number, please try again.")
        except IndexError:
            print("Column number must be between 0-6. Please try again.")


if __name__ == "__main__":
    game = Connect4Game()
    while game.running:
        game.print_grid()
        game.ask_for_input()
