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
        column = ai_service.choose_column()
        game_service.update_grid(game_service.game_grid, column, False)
    print("Board at the end:")
    print("#######################################")
    game_UI.print_grid()
    print("#######################################")
