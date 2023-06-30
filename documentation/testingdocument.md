# Testing document

## Unit testing

Unit tests currently test that the AI correctly picks columns that would either win the game for it or prevent it from losing. They also test that the victory checking function works correctly. The unit tests can be repeated with the command "poetry run invoke test".

The unit tests make sure that every horizontal and diagonal victory is correctly recognized by the check_win function, making it clear if an error is caused by the minimax function or the check_win function misinforming the minimax algorithm. The AI is provided with a prefilled game board containing a winning line in various directions, and the victory checking method is called on every piece of the winning line. There are also tests to eliminate false positives, calling the method on each piece of a three-in-a-row.

The unit tests also check that the algorithm picks the correct column in immediate situations, where the correct column either wins the game right away for the AI or is the only way to prevent the player from winning on their next turn. There are also unit tests to check that the AI recognizes inevitable victories two moves away with an open-ended two-in-a-row, a guaranteed victory three moves away and a test that it correctly solves an inevitable victory 5 moves away based on a puzzle scenario online.

These tests are performed by providing the AI of the test-module with a prefilled gameboard, and asking it to choose the optimal column for its piece with the minimax-algorithm. For multiple move tests, the game board is updated with the AI's selected move and a predetermined player move, before repeating the process for each move.

There are also some basic unit tests for the UI, but they are not required or part of the course.

### Testing coverage

![](./pictures/CoverageReport.png)

As most of the application is confined to game_ai.py, the amount of files to be tested is low.
