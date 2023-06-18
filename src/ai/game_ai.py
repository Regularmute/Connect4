"""Handles the game logic and AI."""

import random
import copy
import timeit

class GameAI:
    """Represents the game logic in charge of tracking the current game state.
    Attributes:
            game_grid(list): A 2D list of 6 rows and 7 columns. Represesents
                the board state of the game.
            running(bool): True if the game is running,
                False if the game is over.
            search_order(list): The order in which minimax searches for the
                best move.
            depth(int): The depth of the minimax algorithm.
            moves(int): The number of moves performed in the game. Used to
                recognise tied games.
    """
    def __init__(self, depth=4):
        """Initializes the game grid and sets the game to running.

        The game grid is a 2D list of 6 rows and 7 columns. Each empty tile is
        represented by a character:
            '.' = empty tile
            'X' = player piece (human)
            'O' = computer piece

        The main program loop will run while the game is running.

        The search order defines what order the computer will search for an
            optimal move, starting with the middle columns.
        """
        self.game_grid = [['.' for _ in range(7)] for _ in range(6)]
        self.running = True
        self.search_order = [3, 2, 4, 1, 5, 0, 6]
        self.depth = depth
        self.moves = 0

    def update_grid(self, grid, column, player):
        """Updates the grid with a piece dropped by a player.

        Args:
            grid(list): The game grid to update.
            column(int, 0-6): The column number to drop the piece in.
            player(bool): True if the piece is dropped by the player,
                False if dropped by the computer.

        Returns:
            grid: The updated game grid.
            piece_row(int): The row number of the piece dropped.
            piece_column(int): The column number of the piece dropped.
        """
        column = int(column)

        if player:
            piece = "X"
        else:
            piece = "O"
        piece_row = 0
        piece_column = 0

        for row in range(5, -1, -1):
            if grid[row][column] == ".":
                grid[row][column] = piece
                piece_row = row
                piece_column = column
                break
        return (grid, piece_row, piece_column)

    def check_win_including_piece(self, grid, piece_row=5, piece_column=0):
        """Checks if the game has been won with a piece.

        Args:
            piece_column(int): The column number of the last piece dropped.

        Returns:
            True if the game has been won, False if not.
        """

        new_piece = grid[piece_row][piece_column]

        if new_piece == ".":
            return False

        # Check vertical connections
        if piece_row < 3:
            if all(grid[piece_row+i][piece_column] == new_piece for i in range(4)):
                return True

        # Check horizontal connections
        for column in range(max(0, piece_column-3), min(4, piece_column+1)):
            if all(
                grid[piece_row][column+i]
                == new_piece for i in range(4)
                ):
                return True

        # Check falling diagonal connections
        for row in range(max(0, piece_row-3), min(3, piece_row+1)):
            for column in range(
                max(0,piece_column-3), min(4, piece_column+1)
                ):
                if all(
                    grid[row+i][column+i]
                    == new_piece for i in range(4)
                    ):
                    return True

        # Check rising diagonal connections
        for row in range(min(5, piece_row+3), max(4, piece_row-1), -1):
            for column in range(
                max(0,piece_column-3), min(4, piece_column+1)
                ):
                if all(
                    grid[row-i][column+i]
                    == new_piece for i in range(4)):
                    return True
        return False

    def choose_column_random(self):
        """Chooses a random column to drop a piece in.

        Returns:
            column(int): The column number to drop the piece in.
        """
        column = random.randint(0, 6)
        while self.game_grid[0][column] != ".":
            column = random.randint(0, 6)
        return column

    def choose_column(self):
        """Chooses a column to drop a piece in using the minimax algorithm.

        Returns:
            column(int): The column number to drop the piece in.
        """
        best_value = -10000
        best_column = 0
        extra_depth = 0
        start_time = timeit.default_timer()
        elapsed_time = 0
        while elapsed_time < 1:
            for column in self.search_order:
                fake_grid = copy.deepcopy(self.game_grid)
                if fake_grid[0][column] == ".":
                    value = self.minimax(
                        self.update_grid(
                            fake_grid, column, False), self.depth + extra_depth, -10000, 10000, False, self.moves)
                    if not value:
                        value = 0
                    if value > best_value:
                        best_value = value
                        best_column = column
            extra_depth += 1
            print("elapsed_time: ", elapsed_time)
            elapsed_time = timeit.default_timer() - start_time
        print("Computer chose column ", str(best_column + 1))
        print("Time elapsed: ", str(elapsed_time))
        print("Depth reached: ", self.depth + extra_depth)
        return best_column

    def evaluate(self, game_state):
        """Evaluates how beneficial the game state is for the AI.

        The function calculates the amount of 3-in-a-row threats for each
        side and subtracts the player's threats from the AI's threats to
        determine the state's "value".

        Args:
            game_state(list): The game grid to evaluate, and the coordinates of its last piece.

        Returns:
            score(int): The score of the game state.
        """

        if self.check_win_including_piece(game_state[0], game_state[1], game_state[2]):
            if game_state[0][game_state[1]][game_state[2]] == "X":
                return -10000
            return 10000

        game_grid = game_state[0]

        ai_threats = 0
        player_threats = 0

        # Count vertical threats
        for row in range(1,3):
            for column in range(7):
                if game_grid[row][column] == "X":
                    if game_grid[row+1][column] == "X" and \
                        game_grid[row+2][column] == "X":
                        player_threats += 1
                if game_grid[row][column] == "O":
                    if game_grid[row+1][column] == "O" and \
                        game_grid[row+2][column] == "O":
                        ai_threats += 1

        # Count horizontal threats
        for row in range(6):
            for column in range(1,4):
                if game_grid[row][column] == "X":
                    if game_grid[row][column+1] == "X" and \
                        game_grid[row][column+2] == "X":
                        player_threats += 1
                if game_grid[row][column] == "O":
                    if game_grid[row][column+1] == "O" and \
                        game_grid[row][column+2] == "O":
                        ai_threats += 1

        # Count rising diagonal threats
        for row in range(1,3):
            for column in range(3,7):
                if game_grid[row][column] == "X":
                    if game_grid[row+1][column-1] == "X" and \
                        game_grid[row+2][column-2] == "X":
                        player_threats += 1
                if game_grid[row][column] == "O":
                    if game_grid[row+1][column-1] == "O" and \
                        game_grid[row+2][column-2] == "O":
                        ai_threats += 1

        # Count falling diagonal threats
        for row in range(1,3):
            for column in range(4):
                if game_grid[row][column] == "X":
                    if game_grid[row+1][column+1] == "X" and \
                        game_grid[row+2][column+2] == "X":
                        player_threats += 1
                if game_grid[row][column] == "O":
                    if game_grid[row+1][column+1] == "O" and \
                        game_grid[row+2][column+2] == "O":
                        ai_threats += 1

        score = ai_threats - player_threats

        return score


    def minimax(self, game_state, depth, alpha, beta, maximizing_player, moves):
        """Returns the optimal column for a dropped piece in a game state.

        Args:
            game_state(list): List with the game grid, last dropped piece's
                row and column of the piece.
            depth(int): The depth of the tree to search.
            alpha(int): The alpha value for alpha-beta pruning: the best value
                found so far for an attainable game state.
            beta(int): The beta value for alpha-beta pruning.
            maximizing_player(bool): True if next move is by the maximizer,
                False if next move is by the minimizer.
            moves(int): The amount of moves made in the hypothetical game
                state. Recognizes a draw at 42 moves.

        Returns:
            value(int): The heuristical numerical value of the game state.
        """

        if depth == 0:
            return self.evaluate(game_state)
        if moves == 42:
            return 0
        if self.check_win_including_piece(game_state[0], game_state[1], game_state[2]):
            if game_state[0][game_state[1]][game_state[2]] == "O":
                return 10000 + depth
            return -10000 - depth
        if maximizing_player:
            value = -10000
            for column in self.search_order:
                fake_grid = copy.deepcopy(game_state[0])
                value = max(value, self.minimax(
                    self.update_grid(fake_grid, column, False),
                    depth-1, alpha, beta, False, moves+1))
                alpha = max(alpha, value)
                if value >= beta:
                    break
            return value
        value = 10000
        for column in self.search_order:
            fake_grid = copy.deepcopy(game_state[0])
            value = min(value, self.minimax(
                self.update_grid(
                    fake_grid, column, True), depth-1, alpha, beta, True, moves+1)
                )
            beta = min(beta, value)
            if value <= alpha:
                break
        return value
