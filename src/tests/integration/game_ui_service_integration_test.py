import unittest
import sys
from io import StringIO
from services.game_service import GameService
from index import GameUI

class TestGameIntegration(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService()
        self.game_ui = GameUI(self.game_service)

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
        self.game_ui.print_grid()
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
        self.game_ui.print_grid()
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
        self.game_ui.print_grid()
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
        self.game_ui.print_grid()
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
        self.game_ui.print_grid()
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
        self.game_ui.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)
