"""Module that runs the game loop.

While the ai-module is running a game, the while_loop is repeated. If either
player wins or if 42 moves have been made without a victory (resulting in a
draw), the game ends and the final game board is printed.

The initial depth of the minimax algorithm can be adjusted by inserting the desired
depth as a parameter of GameAI(). The default value is 4.
"""

from ai.game_ai import GameAI
from ui.game_ui import GameUI

if __name__ == "__main__":
    game_ai = GameAI()
    game_ui = GameUI(game_ai)
    while game_ai.running:
        game_ui.print_grid()
        column = game_ui.get_column_from_player()
        game_state = game_ai.update_grid(game_ai.game_grid, column, True)
        game_ai.moves += 1
        if game_ai.check_win_including_piece(game_ai.game_grid, game_state[1], column):
            print("Player won!")
            game_ai.running = False
        elif game_ai.moves == 42:
            print("Draw!")
            game_ai.running = False
        if not game_ai.running:
            break
        column = game_ai.choose_column()
        game_state = game_ai.update_grid(game_ai.game_grid, column, False)
        game_ai.moves += 1
        if game_ai.check_win_including_piece(game_ai.game_grid, game_state[1], column):
            print("Computer won!")
            game_ai.running = False
        elif game_ai.moves == 42:
            print("Draw!")
            game_ai.running = False
    print("Board at the end:")
    print("#######################################")
    game_ui.print_grid()
    print("#######################################")
