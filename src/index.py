from ai.game_ai import GameAI
from ui.game_ui import GameUI

if __name__ == "__main__":
    game_ai = GameAI()
    game_ui = GameUI(game_ai)
    while game_ai.running:
        game_ui.print_grid()
        column = game_ui.get_column_from_player()
        game_ai.update_grid(game_ai.game_grid, column, True)
        if game_ai.check_win_including_piece(game_ai.game_grid, column):
            print("Player won!")
            game_ai.running = False
        if not game_ai.running:
            break
        column = game_ai.choose_column()
        game_ai.update_grid(game_ai.game_grid, column, False)
        if game_ai.check_win_including_piece(game_ai.game_grid, column):
            print("Computer won!")
            game_ai.running = False
    print("Board at the end:")
    print("#######################################")
    game_ui.print_grid()
    print("#######################################")
