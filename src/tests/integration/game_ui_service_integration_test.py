import unittest
import sys
from io import StringIO
from ai.game_ai import GameAI
from index import GameUI

class TestGameIntegration(unittest.TestCase):
    def setUp(self):
        self.game_ai = GameAI()
        self.game_ui = GameUI(self.game_ai)

    def test_initial_grid_is_printed_correctly(self):
        expected_output = ("[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]\n"
        )
        output = StringIO()
        sys.stdout = output
        self.game_ui.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_one_player_piece(self):
        expected_output = ("[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[1, 0, 0, 0, 0, 0, 0]\n"
        )

        self.game_ai.update_grid(self.game_ai.game_grid, 0, True)

        output = StringIO()
        sys.stdout = output
        self.game_ui.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_two_player_pieces(self):
        expected_output = ("[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 1, 0, 0, 0]"
            +"\n[0, 0, 0, 1, 0, 0, 0]\n"
        )

        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)

        output = StringIO()
        sys.stdout = output
        self.game_ui.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_one_computer_piece(self):
        expected_output = ("[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 2, 0, 0, 0, 0, 0]\n"
        )

        self.game_ai.update_grid(self.game_ai.game_grid, 1, False)

        output = StringIO()
        sys.stdout = output
        self.game_ui.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_two_computer_pieces(self):
        expected_output = ("[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 2, 0, 0]"
            +"\n[0, 0, 0, 0, 2, 0, 0]\n"
        )

        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, False)

        output = StringIO()
        sys.stdout = output
        self.game_ui.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_two_pieces_from_both_sides(self):
        expected_output = ("[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 0, 0, 0, 0]"
            +"\n[0, 0, 0, 2, 0, 0, 0]"
            +"\n[0, 0, 2, 1, 1, 0, 0]\n"
        )

        self.game_ai.update_grid(self.game_ai.game_grid, 3, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 3, False)
        self.game_ai.update_grid(self.game_ai.game_grid, 4, True)
        self.game_ai.update_grid(self.game_ai.game_grid, 2, False)

        output = StringIO()
        sys.stdout = output
        self.game_ui.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)
