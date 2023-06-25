# Testing document


## Unit testing

Unit tests currently test that the AI correctly picks columns that would either win the game for it or prevent it from losing. They also test that the victory checking function works correctly.

The unit tests make sure that every horizontal and diagonal victory is correctly recognized by the check_win function, making it clear if an error is caused by the minimax function or the check_win function misinforming the minimax algorithm.

The unit test also checks that the algorithm picks the correct column in immediate situations, where the correct column either wins the game right away for the AI or is the only way to prevent the player from winning on their next turn. There are also unit tests to check that the AI recognizes inevitable victories two moves away with an open-ended two-in-a-row, and a test that it correctly solves an inevitable victory 5 moves away based on a puzzle scenario online.

There are also some basic unit tests for the UI, but they are not required or part of the course.

### Testing coverage

![](./pictures/CoverageReport.png)

As most of the application is confined to game_ai.py, the amount of files to be tested is low.

## Performance testing

IMPORTANT: I have been informed that performance testing isn't required for this topic, so this section hasn't been updated since June 11th, and could be considered outdated. I still find it interesting to preserve the results to see the change in the AI's current version. During this time, the algorithm performed searches with a fixed depth level, rather than using iterative deepening like in its current version.

### Outdated section begins:

As the only scaling variable in the program is the depth of the minimax queries, the time taken for the AI to choose a move is measured by the code in src/minimax_performance.py. Please note that this test currently always assumes an empty game board, so the times may vary with different game states.

The measurements were done with the assistance of the Python Library timeit, which executes the AI-class's method "choose_column" 100 times, and prints out the average time taken to choose a move.

These tests were performed on a 2,7 GHz Dual-Core Intel Core i5 processor running on macOS Monterey. The hardware is relatively old, so performance may improve on a more modern device. The tests can be replicated after installing the necessary poetry dependencies with the command

`poetry run invoke test-performance`

Here are the current results:

|Minimax Depth|Time taken to choose column (s)|Testing Day|
|-|-|-|
|2|0.01176432135000141|11.6.2023|
|3|0.04542365977999907|11.6.2023|
|4|0.0789036874600015|11.6.2023|
|5|0.235107686299998|11.6.2023|
|6|0.4979836556100008|11.6.2023|
|7|1.9416485094700011|11.6.2023|
|8|4.160757938810002|11.6.2023|

![](./pictures/perftestlinegraph1.svg)

Currently the time complexity of the algorithm seems to be O^n, as expected of the minimax-algorithm.

Worth noting is that the minimax algorithm doesn't reach victory or loss states on the board at lower depths, and the current heuristic for determining the "value" of a board state is not complete. As the heuristics improve, we may see changes in the results, though I don't expect dramatic changes.
