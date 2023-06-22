import unittest
from ai.game_ai import GameAI

class TestGameAI(unittest.TestCase):
    def setUp(self):
        self.game_ai = GameAI()

    # Tests for the AI recognizing whether or not someone has won in a game board.
    # Some tests have been made through "accurate moves" with the actual board
    #   updating function, and many have been by directly placing the tiles on
    #   the board.

    def test_check_win_including_piece_returns_false_for_empty_grid(self):
        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,0))

    # Tests for AI recognizing horizontal victories, starting on row 5 (bottom row)

    def test_check_win_including_piece_returns_true_for_horizontal_win(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,0))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,3))

    def test_check_win_including_piece_returns_true_for_horizontal_win_2(self):
        self.game_ai.game_grid[5][1] = 1
        self.game_ai.game_grid[5][2] = 1
        self.game_ai.game_grid[5][3] = 1
        self.game_ai.game_grid[5][4] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,4))

    def test_check_win_including_piece_returns_true_for_horizontal_win_3(self):
        self.game_ai.game_grid[5][2] = 1
        self.game_ai.game_grid[5][3] = 1
        self.game_ai.game_grid[5][4] = 1
        self.game_ai.game_grid[5][5] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,5))

    def test_check_win_including_piece_returns_true_for_horizontal_win_4(self):
        self.game_ai.game_grid[5][3] = 1
        self.game_ai.game_grid[5][4] = 1
        self.game_ai.game_grid[5][5] = 1
        self.game_ai.game_grid[5][6] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,5))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,6))

    # Horizontal victories on row 4

    def test_check_win_including_piece_returns_true_for_horizontal_win_5(self):
        self.game_ai.game_grid[4][0] = 1
        self.game_ai.game_grid[4][1] = 1
        self.game_ai.game_grid[4][2] = 1
        self.game_ai.game_grid[4][3] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,0))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,3))

    def test_check_win_including_piece_returns_true_for_horizontal_win_6(self):
        self.game_ai.game_grid[4][1] = 1
        self.game_ai.game_grid[4][2] = 1
        self.game_ai.game_grid[4][3] = 1
        self.game_ai.game_grid[4][4] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,4))

    def test_check_win_including_piece_returns_true_for_horizontal_win_7(self):
        self.game_ai.game_grid[4][2] = 1
        self.game_ai.game_grid[4][3] = 1
        self.game_ai.game_grid[4][4] = 1
        self.game_ai.game_grid[4][5] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,5))

    def test_check_win_including_piece_returns_true_for_horizontal_win_8(self):
        self.game_ai.game_grid[4][3] = 1
        self.game_ai.game_grid[4][4] = 1
        self.game_ai.game_grid[4][5] = 1
        self.game_ai.game_grid[4][6] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,5))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,6))

    # Horizontal victories on row 3

    def test_check_win_including_piece_returns_true_for_horizontal_win_9(self):
        self.game_ai.game_grid[3][0] = 1
        self.game_ai.game_grid[3][1] = 1
        self.game_ai.game_grid[3][2] = 1
        self.game_ai.game_grid[3][3] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,0))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,3))

    def test_check_win_including_piece_returns_true_for_horizontal_win_10(self):
        self.game_ai.game_grid[3][1] = 1
        self.game_ai.game_grid[3][2] = 1
        self.game_ai.game_grid[3][3] = 1
        self.game_ai.game_grid[3][4] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,4))

    def test_check_win_including_piece_returns_true_for_horizontal_win_11(self):
        self.game_ai.game_grid[3][2] = 1
        self.game_ai.game_grid[3][3] = 1
        self.game_ai.game_grid[3][4] = 1
        self.game_ai.game_grid[3][5] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,5))

    def test_check_win_including_piece_returns_true_for_horizontal_win_12(self):
        self.game_ai.game_grid[3][3] = 1
        self.game_ai.game_grid[3][4] = 1
        self.game_ai.game_grid[3][5] = 1
        self.game_ai.game_grid[3][6] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,5))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,6))

    # Horizontal victories on row 2
    def test_check_win_including_piece_returns_true_for_horizontal_win_13(self):
        self.game_ai.game_grid[2][0] = 1
        self.game_ai.game_grid[2][1] = 1
        self.game_ai.game_grid[2][2] = 1
        self.game_ai.game_grid[2][3] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,0))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,3))

    def test_check_win_including_piece_returns_true_for_horizontal_win_14(self):
        self.game_ai.game_grid[2][1] = 1
        self.game_ai.game_grid[2][2] = 1
        self.game_ai.game_grid[2][3] = 1
        self.game_ai.game_grid[2][4] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,4))

    def test_check_win_including_piece_returns_true_for_horizontal_win_15(self):
        self.game_ai.game_grid[2][2] = 1
        self.game_ai.game_grid[2][3] = 1
        self.game_ai.game_grid[2][4] = 1
        self.game_ai.game_grid[2][5] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,5))

    def test_check_win_including_piece_returns_true_for_horizontal_win_16(self):
        self.game_ai.game_grid[2][3] = 1
        self.game_ai.game_grid[2][4] = 1
        self.game_ai.game_grid[2][5] = 1
        self.game_ai.game_grid[2][6] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,5))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,6))

    # Horizontal victories on row 1
    def test_check_win_including_piece_returns_true_for_horizontal_win_17(self):
        self.game_ai.game_grid[1][0] = 1
        self.game_ai.game_grid[1][1] = 1
        self.game_ai.game_grid[1][2] = 1
        self.game_ai.game_grid[1][3] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,0))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,3))

    def test_check_win_including_piece_returns_true_for_horizontal_win_18(self):
        self.game_ai.game_grid[1][1] = 1
        self.game_ai.game_grid[1][2] = 1
        self.game_ai.game_grid[1][3] = 1
        self.game_ai.game_grid[1][4] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,4))

    def test_check_win_including_piece_returns_true_for_horizontal_win_19(self):
        self.game_ai.game_grid[1][2] = 1
        self.game_ai.game_grid[1][3] = 1
        self.game_ai.game_grid[1][4] = 1
        self.game_ai.game_grid[1][5] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,5))

    def test_check_win_including_piece_returns_true_for_horizontal_win_20(self):
        self.game_ai.game_grid[1][3] = 1
        self.game_ai.game_grid[1][4] = 1
        self.game_ai.game_grid[1][5] = 1
        self.game_ai.game_grid[1][6] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,5))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,6))

    # Horizontal victories on row 0 (top row)
    def test_check_win_including_piece_returns_true_for_horizontal_win_21(self):
        self.game_ai.game_grid[0][0] = 1
        self.game_ai.game_grid[0][1] = 1
        self.game_ai.game_grid[0][2] = 1
        self.game_ai.game_grid[0][3] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,0))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,3))

    def test_check_win_including_piece_returns_true_for_horizontal_win_22(self):
        self.game_ai.game_grid[0][1] = 1
        self.game_ai.game_grid[0][2] = 1
        self.game_ai.game_grid[0][3] = 1
        self.game_ai.game_grid[0][4] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,4))

    def test_check_win_including_piece_returns_true_for_horizontal_win_23(self):
        self.game_ai.game_grid[0][2] = 1
        self.game_ai.game_grid[0][3] = 1
        self.game_ai.game_grid[0][4] = 1
        self.game_ai.game_grid[0][5] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,5))

    def test_check_win_including_piece_returns_true_for_horizontal_win_24(self):
        self.game_ai.game_grid[0][3] = 1
        self.game_ai.game_grid[0][4] = 1
        self.game_ai.game_grid[0][5] = 1
        self.game_ai.game_grid[0][6] = 1

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,5))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,6))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,0))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,1))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,2))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,3))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,4))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,5))

    def test_check_win_including_piece_returns_true_for_vertical_win_at_column_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,6))

    # Tests that AI recognizes rising diagonals. Starting with the ones
    # beginning on row 5 (bottom row).

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

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,0))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,3))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_2(self):
        self.game_ai.game_grid[5][1] = 2
        self.game_ai.game_grid[4][2] = 2
        self.game_ai.game_grid[3][3] = 2
        self.game_ai.game_grid[2][4] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,4))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_3(self):
        self.game_ai.game_grid[5][2] = 2
        self.game_ai.game_grid[4][3] = 2
        self.game_ai.game_grid[3][4] = 2
        self.game_ai.game_grid[2][5] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,5))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_4(self):
        self.game_ai.game_grid[5][3] = 2
        self.game_ai.game_grid[4][4] = 2
        self.game_ai.game_grid[3][5] = 2
        self.game_ai.game_grid[2][6] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,5))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,6))

    # Tests that AI spots rising diagonal victories starting from row 4
    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_5(self):
        self.game_ai.game_grid[4][0] = 2
        self.game_ai.game_grid[3][1] = 2
        self.game_ai.game_grid[2][2] = 2
        self.game_ai.game_grid[1][3] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,0))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,3))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_6(self):
        self.game_ai.game_grid[4][1] = 2
        self.game_ai.game_grid[3][2] = 2
        self.game_ai.game_grid[2][3] = 2
        self.game_ai.game_grid[1][4] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,4))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_7(self):
        self.game_ai.game_grid[4][2] = 2
        self.game_ai.game_grid[3][3] = 2
        self.game_ai.game_grid[2][4] = 2
        self.game_ai.game_grid[1][5] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,5))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_8(self):
        self.game_ai.game_grid[4][3] = 2
        self.game_ai.game_grid[3][4] = 2
        self.game_ai.game_grid[2][5] = 2
        self.game_ai.game_grid[1][6] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,5))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,6))

    # Tests that AI spots rising diagonal victories starting from row 3
    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_9(self):
        self.game_ai.game_grid[3][0] = 2
        self.game_ai.game_grid[2][1] = 2
        self.game_ai.game_grid[1][2] = 2
        self.game_ai.game_grid[0][3] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,0))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,3))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_10(self):
        self.game_ai.game_grid[3][1] = 2
        self.game_ai.game_grid[2][2] = 2
        self.game_ai.game_grid[1][3] = 2
        self.game_ai.game_grid[0][4] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,1))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,4))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_11(self):
        self.game_ai.game_grid[3][2] = 2
        self.game_ai.game_grid[2][3] = 2
        self.game_ai.game_grid[1][4] = 2
        self.game_ai.game_grid[0][5] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,2))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,5))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win_12(self):
        self.game_ai.game_grid[3][3] = 2
        self.game_ai.game_grid[2][4] = 2
        self.game_ai.game_grid[1][5] = 2
        self.game_ai.game_grid[0][6] = 2

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,3))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,2,4))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,1,5))
        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,6))

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

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,4))

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

        self.assertTrue(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,6))

    def test_check_win_including_piece_returns_false_for_three_horizontal_pieces(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,2))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,5,0))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,1))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,2))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,3))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,4))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,5))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces_at_column_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,6))

    def test_check_win_including_piece_returns_false_for_three_rising_diagonal_pieces(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,3,2))

    def test_check_win_including_piece_returns_false_for_three_rising_diagonal_pieces_2(self):

        """ Tests the following game board:
            ['.', '.', 'X', '.', 'O', '.', '.'],
            ['.', '.', 'O', 'O', 'X', '.', '.'],
            ['.', '.', 'O', 'O', 'X', '.', '.'],
            ['.', 'X', 'O', 'X', 'X', '.', '.'],
            ['.', 'X', 'X', 'O', 'O', 'X', '.'],
            ['.', 'O', 'O', 'X', 'X', 'O', '.']

            The program erroneously announced computer victory after it placed
                a piece on row 0, column 4 (top row, 5th tile).
        """

        self.game_ai.game_grid[0][2] = 1
        self.game_ai.game_grid[0][4] = 2

        self.game_ai.game_grid[1][2] = 2
        self.game_ai.game_grid[1][3] = 2
        self.game_ai.game_grid[1][4] = 1

        self.game_ai.game_grid[2][2] = 2
        self.game_ai.game_grid[2][3] = 2
        self.game_ai.game_grid[2][4] = 1

        self.game_ai.game_grid[3][1] = 1
        self.game_ai.game_grid[3][2] = 2
        self.game_ai.game_grid[3][3] = 1
        self.game_ai.game_grid[3][4] = 1

        self.game_ai.game_grid[4][1] = 1
        self.game_ai.game_grid[4][2] = 1
        self.game_ai.game_grid[4][3] = 2
        self.game_ai.game_grid[4][4] = 2
        self.game_ai.game_grid[4][5] = 1

        self.game_ai.game_grid[5][1] = 2
        self.game_ai.game_grid[5][2] = 2
        self.game_ai.game_grid[5][3] = 1
        self.game_ai.game_grid[5][4] = 1
        self.game_ai.game_grid[5][5] = 2

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,0,4))

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

        self.assertFalse(self.game_ai.check_win_including_piece(self.game_ai.game_grid,4,3))

    # Tests that AI selects a column that leads to victory.

    def test_choose_column_returns_winning_column_horizontally(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.assertEqual(self.game_ai.choose_column(), 3)
    
    def test_choose_column_returns_winning_column_horizontally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)

        self.assertEqual(self.game_ai.choose_column(), 2 or 6)

    def test_choose_column_returns_winning_column_horizontally_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column(), 3)

    def test_choose_column_returns_winning_column_vertically_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)

        self.assertEqual(self.game_ai.choose_column(), 0)

    def test_choose_column_returns_winning_column_vertically_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)

        self.assertEqual(self.game_ai.choose_column(), 1)

    def test_choose_column_returns_winning_column_vertically_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.assertEqual(self.game_ai.choose_column(), 2)

    def test_choose_column_returns_winning_column_vertically_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.assertEqual(self.game_ai.choose_column(), 3)

    def test_choose_column_returns_winning_column_vertically_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)

        self.assertEqual(self.game_ai.choose_column(), 4)

    def test_choose_column_returns_winning_column_vertically_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)

        self.assertEqual(self.game_ai.choose_column(), 5)

    def test_choose_column_returns_winning_column_vertically_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column(), 6)

    def test_choose_column_returns_winning_column_rising_diagonally(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)


        self.assertEqual(self.game_ai.choose_column(), 3)

    def test_choose_column_returns_winning_column_rising_diagonally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column(), 4)

    def test_choose_column_returns_winning_column_falling_diagonally(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.assertEqual(self.game_ai.choose_column(), 3)

    def test_choose_column_returns_winning_column_falling_diagonally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column(), 5)

    # Tests that AI blocks imminent wins by player

    def test_choose_column_returns_column_preventing_player_win_vertically_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.assertEqual(self.game_ai.choose_column(), 0)

    def test_choose_column_returns_column_preventing_player_win_vertically_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.assertEqual(self.game_ai.choose_column(), 1)

    def test_choose_column_returns_column_preventing_player_win_vertically_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertEqual(self.game_ai.choose_column(), 2)

    def test_choose_column_returns_column_preventing_player_win_vertically_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertEqual(self.game_ai.choose_column(), 3)

    def test_choose_column_returns_column_preventing_player_win_vertically_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.assertEqual(self.game_ai.choose_column(), 4)

    def test_choose_column_returns_column_preventing_player_win_vertically_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.assertEqual(self.game_ai.choose_column(), 5)

    def test_choose_column_returns_column_preventing_player_win_vertically_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertEqual(self.game_ai.choose_column(), 6)

    def test_choose_column_returns_column_preventing_player_win_horizontally_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertEqual(self.game_ai.choose_column(), 3)

    def test_choose_column_returns_column_preventing_player_win_horizontally_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertEqual(self.game_ai.choose_column(), 4)

    def test_choose_column_returns_column_preventing_player_win_horizontally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.assertEqual(self.game_ai.choose_column(), 5)

    def test_choose_column_returns_column_preventing_player_win_horizontally_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.assertEqual(self.game_ai.choose_column(), 6)

    def test_choose_column_returns_column_preventing_player_win_horizontally_4(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.assertEqual(self.game_ai.choose_column(), 3)

    def test_choose_column_returns_column_preventing_player_win_horizontally_5(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.assertEqual(self.game_ai.choose_column(), 2)

    def test_choose_column_returns_column_preventing_player_win_horizontally_6(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.assertEqual(self.game_ai.choose_column(), 1)

    def test_choose_column_returns_column_preventing_player_win_horizontally_7(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.assertEqual(self.game_ai.choose_column(), 0)

    def test_choose_column_returns_column_preventing_player_win_rising_diagonally_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.assertEqual(self.game_ai.choose_column(), 3)

    def test_choose_column_returns_column_preventing_player_win_rising_diagonally_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)

        self.assertEqual(self.game_ai.choose_column(), 4)

    def test_choose_column_returns_column_preventing_player_win_rising_diagonally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)

        self.assertEqual(self.game_ai.choose_column(), 5)

    def test_choose_column_returns_column_preventing_player_win_rising_diagonally_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 6, False)

        self.assertEqual(self.game_ai.choose_column(), 6)

    def test_choose_column_returns_column_preventing_player_win_falling_diagonally_0(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 6, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 5, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)

        self.assertEqual(self.game_ai.choose_column(), 3)

    def test_choose_column_returns_column_preventing_player_win_falling_diagonally_1(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 5, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        self.assertEqual(self.game_ai.choose_column(), 2)

    def test_choose_column_returns_column_preventing_player_win_falling_diagonally_2(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)

        self.assertEqual(self.game_ai.choose_column(), 1)

    def test_choose_column_returns_column_preventing_player_win_falling_diagonally_3(self):
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 1, True)

        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 0, False)

        self.assertEqual(self.game_ai.choose_column(), 0)
