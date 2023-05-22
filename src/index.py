class Connect4Game:
    def __init__(self):
        self.game_grid = [['.' for _ in range(7)] for _ in range(6)]  
        self.running = True 

    def print_grid(self):
        for row in self.game_grid:
            print(row)
    
    def update_grid(self, column, player):
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
        print("Please enter a column number (1-7): ")
        try:
            column = int(input()) - 1
            if column < 0 or column > 6:
                print("Invalid column number, please try again.")
            elif self.game_grid[0][column] != ".":
                print("Column is full, please choose another.")
            elif column == -1:
                self.running = False
            else:
                self.update_grid(column, True)
        except ValueError:
            print("Invalid column number, please try again.")


if __name__ == "__main__":
    game = Connect4Game()
    while game.running:
        game.print_grid()
        game.ask_for_input()
