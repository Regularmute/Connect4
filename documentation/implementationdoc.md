# Implementation Document

## Project Structure

The application is split into three parts: Graphical User Interface, AI and the main file running the game loop. A separate directory has been made for unit testing, and another test file for performance testing is located together with the main file.

## Implemented time and space complexities

Currently the time complexity of the minimax function is O^n as expected. The space complexity is O^n, since the game grid is copied with each minimax iteration to explore possible game states.

## Flaws and possible improvements

The heuristic evaluation of different game states is very minimal, only evaluating the amount of 3-in-a-rows, but current attempts to sophisticate it have reduced the depth reached by the minimax algorithm with iterative deepening.

## Sources
* Line chart demonstrating performance test results made with [RapidTables](https://www.rapidtables.com/tools/line-graph.html)
* Course material for minimax: https://tiralabra.github.io/2023_alkukesa/fi/aiheet/minimax.pdf
* Wikipedia articles:
    * https://en.wikipedia.org/wiki/Minimax
    * https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    * https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search
