"""Module that tests the performance of the minimax algorithm.

The algorithm can be tested with different depths by changing the parameter
of GameAI(). The default depth is 4.
"""

import timeit

test_code = """
from ai.game_ai import GameAI

test_AI = GameAI()
test_AI.choose_column()
"""

if __name__=="__main__":
    time = timeit.timeit(test_code, number=100)
    print("Average time taken to choose a column: ", time/100)
    print(" seconds.")
