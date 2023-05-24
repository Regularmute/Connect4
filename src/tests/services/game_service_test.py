import unittest
import sys
from io import StringIO
from services.game_service import GameService

class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService()

    def test_initial_grid_is_printed_correctly(self):
        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']\n"
        )
        output = StringIO()
        sys.stdout = output
        self.game_service.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_one_player_piece(self):
        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['X', '.', '.', '.', '.', '.', '.']\n"
        )

        self.game_service.update_grid(0, True)

        output = StringIO()
        sys.stdout = output
        self.game_service.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_two_player_pieces(self):
        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', 'X', '.', '.', '.']"
            +"\n['.', '.', '.', 'X', '.', '.', '.']\n"
        )

        self.game_service.update_grid(3, True)
        self.game_service.update_grid(3, True)

        output = StringIO()
        sys.stdout = output
        self.game_service.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_one_computer_piece(self):

        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', 'O', '.', '.', '.', '.', '.']\n"
        )

        self.game_service.update_grid(1, False)

        output = StringIO()
        sys.stdout = output
        self.game_service.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_two_computer_pieces(self):

        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', 'O', '.', '.']"
            +"\n['.', '.', '.', '.', 'O', '.', '.']\n"
        )

        self.game_service.update_grid(4, False)
        self.game_service.update_grid(4, False)

        output = StringIO()
        sys.stdout = output
        self.game_service.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_two_pieces_from_both_sides(self):

        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', 'O', '.', '.', '.']"
            +"\n['.', '.', 'O', 'X', 'X', '.', '.']\n"
        )

        self.game_service.update_grid(3, True)
        self.game_service.update_grid(3, False)
        self.game_service.update_grid(4, True)
        self.game_service.update_grid(2, False)

        output = StringIO()
        sys.stdout = output
        self.game_service.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_check_win_including_piece_returns_false_for_empty_grid(self):

        self.assertFalse(self.game_service.check_win_including_piece())

    def test_check_win_including_piece_returns_true_for_horizontal_win(self):

        self.game_service.update_grid(0, True)
        self.game_service.update_grid(1, True)
        self.game_service.update_grid(2, True)
        self.game_service.update_grid(3, True)

        self.assertTrue(self.game_service.check_win_including_piece(5,3))

    def test_check_win_including_piece_returns_true_for_vertical_win(self):

        self.game_service.update_grid(0, True)
        self.game_service.update_grid(0, True)
        self.game_service.update_grid(0, True)
        self.game_service.update_grid(0, True)

        self.assertTrue(self.game_service.check_win_including_piece(2,0))

    def test_check_win_including_piece_returns_true_for_rising_diagonal_win(self):

        self.game_service.update_grid(0, True)

        self.game_service.update_grid(1, False)
        self.game_service.update_grid(1, True)

        self.game_service.update_grid(2, False)
        self.game_service.update_grid(2, False)
        self.game_service.update_grid(2, True)

        self.game_service.update_grid(3, False)
        self.game_service.update_grid(3, False)
        self.game_service.update_grid(3, False)
        self.game_service.update_grid(3, True)

        self.assertTrue(self.game_service.check_win_including_piece(2,3))

    def test_check_win_including_piece_returns_true_for_falling_diagonal_win(self):

        self.game_service.update_grid(1, False)
        self.game_service.update_grid(1, False)
        self.game_service.update_grid(1, False)
        self.game_service.update_grid(1, True)

        self.game_service.update_grid(2, False)
        self.game_service.update_grid(2, False)
        self.game_service.update_grid(2, True)

        self.game_service.update_grid(3, False)
        self.game_service.update_grid(3, True)

        self.game_service.update_grid(4, True)

        self.assertTrue(self.game_service.check_win_including_piece(0,4))

    def test_check_win_including_piece_returns_false_for_three_horizontal_pieces(self):

        self.game_service.update_grid(0, True)
        self.game_service.update_grid(1, True)
        self.game_service.update_grid(2, True)

        self.assertFalse(self.game_service.check_win_including_piece(0,2))

    def test_check_win_including_piece_returns_false_for_three_vertical_pieces(self):

        self.game_service.update_grid(0, True)
        self.game_service.update_grid(0, True)
        self.game_service.update_grid(0, True)

        self.assertFalse(self.game_service.check_win_including_piece(2,0))

    def test_check_win_including_piece_returns_false_for_three_rising_diagonal_pieces(self):

        self.game_service.update_grid(0, True)

        self.game_service.update_grid(1, False)
        self.game_service.update_grid(1, True)

        self.game_service.update_grid(2, False)
        self.game_service.update_grid(2, False)
        self.game_service.update_grid(2, True)

        self.assertFalse(self.game_service.check_win_including_piece(3,2))

    def test_check_win_including_piece_returns_false_for_three_falling_diagonal_pieces(self):

        self.game_service.update_grid(1, False)
        self.game_service.update_grid(1, False)
        self.game_service.update_grid(1, False)
        self.game_service.update_grid(1, True)

        self.game_service.update_grid(2, False)
        self.game_service.update_grid(2, False)
        self.game_service.update_grid(2, True)

        self.game_service.update_grid(3, False)
        self.game_service.update_grid(3, True)

        self.assertFalse(self.game_service.check_win_including_piece(4,3))
