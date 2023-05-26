from services.game_service import GameService
from ui.game_ui import GameUI

if __name__ == "__main__":
    game_service = GameService()
    game_UI = GameUI(game_service)
    while game_service.running:
        game_UI.print_grid()
        column = game_UI.get_column_from_player()
        game_service.update_grid(column, True)
        column = game_UI.get_column_from_computer()
        game_service.update_grid(column, False)
