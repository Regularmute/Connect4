import unittest
import sys
from io import StringIO
from index import GameUI

class FakeGameService:
    def __init__(self):
        self.game_grid = self.game_grid = [[0 for _ in range(7)] for _ in range(6)]
        self.running = True

class TestGameIntegration(unittest.TestCase):
    def setUp(self):
        self.game_ui = GameUI(FakeGameService())

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

        self.game_ui.game_service.game_grid[5][0] = 1

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

        self.game_ui.game_service.game_grid[5][3] = 1
        self.game_ui.game_service.game_grid[4][3] = 1

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

        self.game_ui.game_service.game_grid[5][1] = 2

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

        self.game_ui.game_service.game_grid[5][4] = 2
        self.game_ui.game_service.game_grid[4][4] = 2

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

        self.game_ui.game_service.game_grid[5][3] = 1
        self.game_ui.game_service.game_grid[4][3] = 2
        self.game_ui.game_service.game_grid[5][4] = 1
        self.game_ui.game_service.game_grid[5][2] = 2

        output = StringIO()
        sys.stdout = output
        self.game_ui.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)
