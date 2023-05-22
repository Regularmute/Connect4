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
