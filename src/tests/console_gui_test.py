import unittest
import sys
from io import StringIO
from index import Connect4Game

class TestConsoleGui(unittest.TestCase):
    def setUp(self):
        print("Setting up test...")

    def test_initial_grid_is_printed_correctly(self):
        game = Connect4Game()
        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']\n"
        )
        output = StringIO()
        sys.stdout = output
        game.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_one_player_piece(self):
        game = Connect4Game()

        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['X', '.', '.', '.', '.', '.', '.']\n"
        )

        game.update_grid(0, True)

        output = StringIO()
        sys.stdout = output
        game.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_two_player_pieces(self):
        game = Connect4Game()

        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', 'X', '.', '.', '.']"
            +"\n['.', '.', '.', 'X', '.', '.', '.']\n"
        )

        game.update_grid(3, True)
        game.update_grid(3, True)

        output = StringIO()
        sys.stdout = output
        game.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_one_computer_piece(self):
        game = Connect4Game()

        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', 'O', '.', '.', '.', '.', '.']\n"
        )

        game.update_grid(1, False)

        output = StringIO()
        sys.stdout = output
        game.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_two_computer_pieces(self):
        game = Connect4Game()

        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', 'O', '.', '.']"
            +"\n['.', '.', '.', '.', 'O', '.', '.']\n"
        )

        game.update_grid(4, False)
        game.update_grid(4, False)

        output = StringIO()
        sys.stdout = output
        game.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_grid_is_printed_correctly_after_two_pieces_from_both_sides(self):
        game = Connect4Game()

        expected_output = ("['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', '.', '.', '.', '.']"
            +"\n['.', '.', '.', 'O', '.', '.', '.']"
            +"\n['.', '.', 'O', 'X', 'X', '.', '.']\n"
        )

        game.update_grid(3, True)
        game.update_grid(3, False)
        game.update_grid(4, True)
        game.update_grid(2, False)

        output = StringIO()
        sys.stdout = output
        game.print_grid()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)
