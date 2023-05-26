import random
import copy

class Connect4AI:
    """Artificial intelligence for the game.

    Attributes:
        game_service(GameService): The game logic with the game's information.
    """

    def __init__(self, game_service):
        self.game_service = game_service

    def choose_column(self):
        """Chooses a random column to drop a piece in.

        Returns:
            column(int): The column number to drop the piece in.
        """
        column = random.randint(0, 6)
        while self.game_service.game_grid[0][column] != ".":
            column = random.randint(0, 6)
        return column

    def choose_column_minimax(self):
        """Chooses a column to drop a piece in using the minimax algorithm.

        Returns:
            column(int): The column number to drop the piece in.
        """
        best_value = -10000
        best_column = 0
        fake_grid = copy.deepcopy(self.game_service.game_grid)
        for column in range(7):
            if self.game_service.game_grid[0][column] == ".":
                value = self.minimax(
                    self.game_service.update_grid(
                        fake_grid, column, False), 4, -10000, 10000, True)
                if not value:
                    value = 0
                if not best_value:
                    best_value = value
                if value > best_value:
                    best_value = value
                    best_column = column
        return best_column

    def evaluate(self, game_state):
        """Evaluates how beneficial the game state is for the AI.

        The function calculates the amount of 3-in-a-row threats for each
        side and subtracts the player's threats from the AI's threats to
        determine the state's "value".

        Args:
            game_state(list): The game grid to evaluate.

        Returns:
            score(int): The score of the game state.
        """

        if self.game_service.check_win_including_piece(game_state[1], game_state[2]):
            if self.game_service.game_grid[game_state[1]][game_state[2]] == "X":
                return -10000
            else:
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


    def minimax(self, game_state, depth, alpha, beta, maximizing_player):
        """Returns the optimal column for a dropped piece in a game state.

        Args:
            game_state(list): The game grid to evaluate.
            depth(int): The depth of the tree to search.
            alpha(int): The alpha value for alpha-beta pruning.
            beta(int): The beta value for alpha-beta pruning.
            maximizing_player(bool): True if next move is by the maximizer,
                False if next  move is by the minimizer.
        """
        if depth == 0:
            return self.evaluate(game_state)
        if self.game_service.check_win_including_piece(game_state[1], game_state[2]):
            if self.game_service.game_grid[game_state[1]][game_state[2]] == "O":
                return self.evaluate(game_state) + depth
            else:
                return self.evaluate(game_state) - depth
        if maximizing_player:
            value = -10000
            for column in range(7):
                value = max(value, self.minimax(
                    self.game_service.update_grid(
                        game_state, column, True), depth-1, alpha, beta, False))
                alpha = max(alpha, value)
                if value >= beta:
                    break
                return value
        else:
            value = 10000
            for column in range(7):
                value = min(value, self.minimax(
                    self.game_service.update_grid(
                        game_state, column, True), depth-1, alpha, beta, True)
                    )
                beta = min(beta, value)
                if value <= alpha:
                    break
                return value
