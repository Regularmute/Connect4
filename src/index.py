from services.game_service import game_service

class GameUI:
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
                game_service.update_grid(column, True)
        except ValueError:
            print("Invalid column number, please try again.")
        except IndexError:
            print("Column number must be between 0-6. Please try again.")


if __name__ == "__main__":
    game_UI = GameUI()
    while game_service.running:
        game_service.print_grid()
        game_UI.ask_for_input()
