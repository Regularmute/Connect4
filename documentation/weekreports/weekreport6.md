# Week 6 (June 19th - June 25th)

## Progress Made

* Fixed check_win working incorrectly with rising diagonals.
* Refactored the gameboard and pieces from strings to integers.
* choose_column first reviews the move that was optimal during the previous depth iteration.
* Added many more tests to thoroughly test check_win, and tests that minimax recognizes wins two and five moves away.
* Fixed alpha-beta pruning: choose_column wasn't updating the alpha value as it should.
* Implemented transposition table to speed up minimax finding best moves for duplicate game board states.
* Adjusted alpha and beta values being updated correctly within minimax function.


## Problems and Questions

* Currently my test for a guaranteed victory in 5 moves is not working, but I feel like I will figure it out.

## Next Steps

* I will create more tests to make sure that the minimax algorithm picks "correct" moves in longer guaranteed victories as well.

## Hours spent

|Date|Hours spent|Work focus|
|---|---|---|
|21.6.|3|fixing tests, refactoring, adding tests for victory checking|
|22.6|4|tests, ordering moves between iterations|
|23.6|1|documentation, ordering moves|
|23.6|2|documentation, ordering moves|
|25.6|2|ordering moves, implementing transposition table, fixing alpha-beta-pruning|
|Total hours:|12|
