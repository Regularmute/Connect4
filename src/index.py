from services.game_service import GameService
from services.ai_service import Connect4AI
from ui.game_ui import GameUI

if __name__ == "__main__":
    game_service = GameService()
    ai_service = Connect4AI(game_service)
    game_UI = GameUI(game_service)
    while game_service.running:
        game_UI.print_grid()
        column = game_UI.get_column_from_player()
        game_service.update_grid(game_service.game_grid, column, True)
        if game_service.check_win_including_piece(game_service.game_grid, column):
            print("Player won!")
            game_service.running = False
        if not game_service.running:
            break
        column = ai_service.choose_column_minimax()
        game_service.update_grid(game_service.game_grid, column, False)
        if game_service.check_win_including_piece(game_service.game_grid, column):
            print("Computer won!")
            game_service.running = False
    print("Board at the end:")
    print("#######################################")
    game_UI.print_grid()
    print("#######################################")
