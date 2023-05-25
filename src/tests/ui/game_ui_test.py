import unittest
import sys
from io import StringIO
from index import GameUI

class FakeGameService:
    def __init__(self):
        self.game_grid = self.game_grid = [['.' for _ in range(7)] for _ in range(6)]
        self.running = True

class TestGameIntegration(unittest.TestCase):
    def setUp(self):
        self.game_ui = GameUI(FakeGameService())

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

        self.game_ui.game_service.game_grid[5][0] = "X"

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

        self.game_ui.game_service.game_grid[5][3] = "X"
        self.game_ui.game_service.game_grid[4][3] = "X"

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

        self.game_ui.game_service.game_grid[5][1] = "O"


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

        self.game_ui.game_service.game_grid[5][4] = "O"
        self.game_ui.game_service.game_grid[4][4] = "O"


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

        self.game_ui.game_service.game_grid[5][3] = "X"
        self.game_ui.game_service.game_grid[4][3] = "O"
        self.game_ui.game_service.game_grid[5][4] = "X"
        self.game_ui.game_service.game_grid[5][2] = "O"


        output = StringIO()
        sys.stdout = output
        self.game_ui.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)
