import unittest
from services.ai_service import Connect4AI
from services.game_service import GameService

class TestAIService(unittest.TestCase):
    def setUp(self):
        self.ai_service = Connect4AI(GameService)

    def test_choose_column_minimax_returns_winning_column_horizontally(self):
        pass
    
    def test_choose_column_minimax_returns_winning_column_horizontally_2(self):
        pass

    def test_choose_column_minimax_returns_winning_column_vertically(self):
        pass

    def test_choose_column_minimax_returns_winning_column_vertically_2(self):
        pass

    def test_choose_column_minimax_returns_winning_column_rising_diagonally(self):
        pass

    def test_choose_column_minimax_returns_winning_column_rising_diagonally_2(self):
        pass

    def test_choose_column_minimax_returns_winning_column_falling_diagonally(self):
        pass

    def test_choose_column_minimax_returns_winning_column_falling_diagonally_2(self):
        pass
