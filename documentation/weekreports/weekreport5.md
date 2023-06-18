# Week 5 (June 12th - June 18th)

## Progress Made

* Fixed a bug with check_win giving false positives on rising diagonals.
* Fixed a bug where the game was printing the wrong column number for which move the computer made.
* Implemented move counting for the AI and recognizing drawn games when the maximum amount of moves were made.
* Added more tests:
    * A specific game board situation with a false positive from check_win.
* Implemented iterative deepening to loop choose_col until total time has reached one second at the end of a loop.
* Experimented with more accurate heuristics, but it seemed to slow down the algorithm to the point of reaching fewer moves to examine.

## Problems and Questions

* I'm a bit confused by the transposition table and ordering moves; are these two separate operations?
    * Should choose_column should first explore the column chosen during the previous depth level? Also should the minimax algorithm also reorder the columns during each iteration?
    * Is the transposition table a dictionary/hash table of key-value pairs(key: game-board-state, value:best column at said board-state) that is filled during each iteration in the minimax algorithm, and then during each loop inside the minimax algorithm it first checks if the board-state it is planning a move for is already in the transposition table, making it possible to determine the best move right away and allow starting the next iteration that much earlier?


## Next Steps

* Implement a transposition table.
* Look into ordering moves.


## Hours spent

|Date|Hours spent|Work focus|
|---|---|---|
|17.6.|1|Documentation, testing, debugging, implementing draws|
|18.6.|3|Refactoring, bug fixing, experimenting heuristics, iterative deepening|
|18.6.|1|Documentation|
|Total hours:|5|
