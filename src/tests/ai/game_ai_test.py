import unittest
from ai.game_ai import GameAI

class TestGameAI(unittest.TestCase):
    def setUp(self):
        self.game_ai = GameAI()

    # Tests for the AI recognizing whether or not someone has won in a game board.

    def test_check_win_including_piece_returns_false_for_empty_grid(self):
        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid, 0))

    def test_check_win_including_piece_returns_true_for_horizontal_win(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3))

    def test_check_win_including_piece_returns_true_for_horizontal_win_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,6))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,6))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_2(self):
        # Checks for rising diagonal win on the right side of the grid
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,6))

    def test_check_win_including_piece_returns_true_for_falling_diagonal_win(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4))

    def test_check_win_including_piece_returns_true_for_falling_diagonal_win_2(self):
        # Checks for falling diagonal wins on the right side of the board
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,6))

    def test_check_win_including_piece_returns_false_for_three_horizontal_pieces(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,6))

    def test_check_win_including_piece_returns_false_for_three_rising_diagonal_pieces(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2))

    def test_check_win_including_piece_returns_false_for_three_falling_diagonal_pieces(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3))

    # Tests that AI selects a column that leads to victory.

    def test_choose_column_minimax_returns_winning_column_horizontally(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 3)
    
    def test_choose_column_minimax_returns_winning_column_horizontally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 2 or 6)

    def test_choose_column_minimax_returns_winning_column_horizontally_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_winning_column_vertically_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 0)

    def test_choose_column_minimax_returns_winning_column_vertically_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 1)

    def test_choose_column_minimax_returns_winning_column_vertically_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 2)

    def test_choose_column_minimax_returns_winning_column_vertically_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_winning_column_vertically_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 4)

    def test_choose_column_minimax_returns_winning_column_vertically_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 5)

    def test_choose_column_minimax_returns_winning_column_vertically_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 6)

    def test_choose_column_minimax_returns_winning_column_rising_diagonally(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)


        self.assertEqual(self.game_ai.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_winning_column_rising_diagonally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 4)

    def test_choose_column_minimax_returns_winning_column_falling_diagonally(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_winning_column_falling_diagonally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 5)

    # Tests that AI blocks imminent wins by player

    def test_choose_column_minimax_returns_column_preventing_player_win_vertically_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 0)

    def test_choose_column_minimax_returns_column_preventing_player_win_vertically_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 1)

    def test_choose_column_minimax_returns_column_preventing_player_win_vertically_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 2)

    def test_choose_column_minimax_returns_column_preventing_player_win_vertically_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_column_preventing_player_win_vertically_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 4)

    def test_choose_column_minimax_returns_column_preventing_player_win_vertically_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 5)

    def test_choose_column_minimax_returns_column_preventing_player_win_vertically_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 6)

    def test_choose_column_minimax_returns_column_preventing_player_win_horizontally_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_column_preventing_player_win_horizontally_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 4)

    def test_choose_column_minimax_returns_column_preventing_player_win_horizontally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 5)

    def test_choose_column_minimax_returns_column_preventing_player_win_horizontally_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 6)

    def test_choose_column_minimax_returns_column_preventing_player_win_horizontally_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_column_preventing_player_win_horizontally_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 2)

    def test_choose_column_minimax_returns_column_preventing_player_win_horizontally_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 1)

    def test_choose_column_minimax_returns_column_preventing_player_win_horizontally_7(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.assertEqual(self.game_ai.choose_column_minimax(), 0)

    def test_choose_column_minimax_returns_column_preventing_player_win_rising_diagonally_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_column_preventing_player_win_rising_diagonally_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 4)

    def test_choose_column_minimax_returns_column_preventing_player_win_rising_diagonally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 5)

    def test_choose_column_minimax_returns_column_preventing_player_win_rising_diagonally_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 6)

    def test_choose_column_minimax_returns_column_preventing_player_win_falling_diagonally_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 3)

    def test_choose_column_minimax_returns_column_preventing_player_win_falling_diagonally_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 2)

    def test_choose_column_minimax_returns_column_preventing_player_win_falling_diagonally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 1)

    def test_choose_column_minimax_returns_column_preventing_player_win_falling_diagonally_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)

        self.assertEqual(self.game_ai.choose_column_minimax(), 0)
