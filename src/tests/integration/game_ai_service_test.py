import unittest
from services.ai_service import Connect4AI
from services.game_service import GameService

class TestAIService(unittest.TestCase):
    def setUp(self):
        self.ai_service = Connect4AI(GameService())
        self.game_service = self.ai_service.game_service

    def test_choose_column_minimax_returns_winning_column_horizontally(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, False)
        self.game_service.update_grid(self.game_service.game_grid, 1, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, False)

        self.assertEqual(self.ai_service.choose_column_minimax(), 3)
    
    def test_choose_column_minimax_returns_winning_column_horizontally_2(self):
        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 4, False)
        self.game_service.update_grid(self.game_service.game_grid, 5, False)

        self.assertEqual(self.ai_service.choose_column_minimax(), 6)

    def test_choose_column_minimax_returns_winning_column_vertically(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, False)
        self.game_service.update_grid(self.game_service.game_grid, 0, False)
        self.game_service.update_grid(self.game_service.game_grid, 0, False)

        self.assertEqual(self.ai_service.choose_column_minimax(), 0)

    def test_choose_column_minimax_returns_winning_column_vertically_2(self):
        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, False)

        self.assertEqual(self.ai_service.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_winning_column_rising_diagonally(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, False)

        self.game_service.update_grid(self.game_service.game_grid, 1, True)
        self.game_service.update_grid(self.game_service.game_grid, 1, False)

        self.game_service.update_grid(self.game_service.game_grid, 2, True)
        self.game_service.update_grid(self.game_service.game_grid, 2, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, False)

        self.game_service.update_grid(self.game_service.game_grid, 3, True)
        self.game_service.update_grid(self.game_service.game_grid, 3, True)
        self.game_service.update_grid(self.game_service.game_grid, 3, True)


        self.assertEqual(self.ai_service.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_winning_column_rising_diagonally_2(self):
        self.game_service.update_grid(self.game_service.game_grid, 3, False)

        self.game_service.update_grid(self.game_service.game_grid, 4, True)

        self.game_service.update_grid(self.game_service.game_grid, 5, True)
        self.game_service.update_grid(self.game_service.game_grid, 5, False)
        self.game_service.update_grid(self.game_service.game_grid, 5, False)

        self.game_service.update_grid(self.game_service.game_grid, 6, True)
        self.game_service.update_grid(self.game_service.game_grid, 6, True)
        self.game_service.update_grid(self.game_service.game_grid, 6, True)
        self.game_service.update_grid(self.game_service.game_grid, 6, False)

        self.assertEqual(self.ai_service.choose_column_minimax(), 4)

    def test_choose_column_minimax_returns_winning_column_falling_diagonally(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, True)
        self.game_service.update_grid(self.game_service.game_grid, 0, False)
        self.game_service.update_grid(self.game_service.game_grid, 0, True)
        self.game_service.update_grid(self.game_service.game_grid, 0, False)

        self.game_service.update_grid(self.game_service.game_grid, 1, True)
        self.game_service.update_grid(self.game_service.game_grid, 1, True)
        self.game_service.update_grid(self.game_service.game_grid, 1, False)

        self.game_service.update_grid(self.game_service.game_grid, 2, True)
        self.game_service.update_grid(self.game_service.game_grid, 2, False)

        self.assertEqual(self.ai_service.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_winning_column_falling_diagonally_2(self):
        self.game_service.update_grid(self.game_service.game_grid, 3, True)
        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, True)
        self.game_service.update_grid(self.game_service.game_grid, 3, False)

        self.game_service.update_grid(self.game_service.game_grid, 4, True)
        self.game_service.update_grid(self.game_service.game_grid, 4, True)
        self.game_service.update_grid(self.game_service.game_grid, 4, False)

        self.game_service.update_grid(self.game_service.game_grid, 5, True)

        self.game_service.update_grid(self.game_service.game_grid, 6, False)

        self.assertEqual(self.ai_service.choose_column_minimax(), 5)
