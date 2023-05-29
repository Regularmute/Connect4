import unittest
from services.game_service import GameService

class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService()

    def test_check_win_including_piece_returns_false_for_empty_grid(self):
        self.assertFalse(self.game_service.check_win_including_piece())

    def test_check_win_including_piece_returns_true_for_horizontal_win(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, True)
        self.game_service.update_grid(self.game_service.game_grid, 1, True)
        self.game_service.update_grid(self.game_service.game_grid, 2, True)
        self.game_service.update_grid(self.game_service.game_grid, 3, True)

        self.assertTrue(self.game_service.check_win_including_piece(5,3))

    def test_check_win_including_piece_returns_true_for_horizontal_win_2(self):
        self.game_service.update_grid(self.game_service.game_grid, 3, True)
        self.game_service.update_grid(self.game_service.game_grid, 4, True)
        self.game_service.update_grid(self.game_service.game_grid, 5, True)
        self.game_service.update_grid(self.game_service.game_grid, 6, True)

        self.assertTrue(self.game_service.check_win_including_piece(5,6))

    def test_check_win_including_piece_returns_true_for_vertical_win(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, True)
        self.game_service.update_grid(self.game_service.game_grid, 0, True)
        self.game_service.update_grid(self.game_service.game_grid, 0, True)
        self.game_service.update_grid(self.game_service.game_grid, 0, True)

        self.assertTrue(self.game_service.check_win_including_piece(2,0))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, True)

        self.game_service.update_grid(self.game_service.game_grid, 1, False)
        self.game_service.update_grid(self.game_service.game_grid, 1, True)

        self.game_service.update_grid(self.game_service.game_grid, 2, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, True)

        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, True)

        self.assertTrue(self.game_service.check_win_including_piece(2,3))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_2(self):
        # Checks for rising diagonal win on the right side of the grid
        self.game_service.update_grid(self.game_service.game_grid, 3, True)

        self.game_service.update_grid(self.game_service.game_grid, 4, False)
        self.game_service.update_grid(self.game_service.game_grid, 4, True)

        self.game_service.update_grid(self.game_service.game_grid, 5, False)
        self.game_service.update_grid(self.game_service.game_grid, 5, False)
        self.game_service.update_grid(self.game_service.game_grid, 5, True)

        self.game_service.update_grid(self.game_service.game_grid, 6, False)
        self.game_service.update_grid(self.game_service.game_grid, 6, False)
        self.game_service.update_grid(self.game_service.game_grid, 6, False)
        self.game_service.update_grid(self.game_service.game_grid, 6, True)

        self.assertTrue(self.game_service.check_win_including_piece(2,6))

    def test_check_win_including_piece_returns_true_for_falling_diagonal_win(self):
        self.game_service.update_grid(self.game_service.game_grid, 1, False)
        self.game_service.update_grid(self.game_service.game_grid, 1, False)
        self.game_service.update_grid(self.game_service.game_grid, 1, False)
        self.game_service.update_grid(self.game_service.game_grid, 1, True)

        self.game_service.update_grid(self.game_service.game_grid, 2, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, True)

        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, True)

        self.game_service.update_grid(self.game_service.game_grid, 4, True)

        self.assertTrue(self.game_service.check_win_including_piece(5,4))

    def test_check_win_including_piece_returns_true_for_falling_diagonal_win_2(self):
        # Checks for falling diagonal wins on the right side of the board
        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, True)

        self.game_service.update_grid(self.game_service.game_grid, 4, False)
        self.game_service.update_grid(self.game_service.game_grid, 4, False)
        self.game_service.update_grid(self.game_service.game_grid, 4, True)

        self.game_service.update_grid(self.game_service.game_grid, 5, False)
        self.game_service.update_grid(self.game_service.game_grid, 5, True)

        self.game_service.update_grid(self.game_service.game_grid, 6, True)

        self.assertTrue(self.game_service.check_win_including_piece(5,6))

    def test_check_win_including_piece_returns_false_for_three_horizontal_pieces(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, True)
        self.game_service.update_grid(self.game_service.game_grid, 1, True)
        self.game_service.update_grid(self.game_service.game_grid, 2, True)

        self.assertFalse(self.game_service.check_win_including_piece(0,2))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, True)
        self.game_service.update_grid(self.game_service.game_grid, 0, True)
        self.game_service.update_grid(self.game_service.game_grid, 0, True)

        self.assertFalse(self.game_service.check_win_including_piece(2,0))

    def test_check_win_including_piece_returns_false_for_three_rising_diagonal_pieces(self):
        self.game_service.update_grid(self.game_service.game_grid, 0, True)

        self.game_service.update_grid(self.game_service.game_grid, 1, False)
        self.game_service.update_grid(self.game_service.game_grid, 1, True)

        self.game_service.update_grid(self.game_service.game_grid, 2, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, True)

        self.assertFalse(self.game_service.check_win_including_piece(3,2))

    def test_check_win_including_piece_returns_false_for_three_falling_diagonal_pieces(self):
        self.game_service.update_grid(self.game_service.game_grid, 1, False)
        self.game_service.update_grid(self.game_service.game_grid, 1, False)
        self.game_service.update_grid(self.game_service.game_grid, 1, False)
        self.game_service.update_grid(self.game_service.game_grid, 1, True)

        self.game_service.update_grid(self.game_service.game_grid, 2, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, False)
        self.game_service.update_grid(self.game_service.game_grid, 2, True)

        self.game_service.update_grid(self.game_service.game_grid, 3, False)
        self.game_service.update_grid(self.game_service.game_grid, 3, True)

        self.assertFalse(self.game_service.check_win_including_piece(4,3))
