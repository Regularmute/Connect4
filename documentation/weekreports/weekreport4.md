# Week 4 (June 5th - June 11th)

## Progress Made

* GameService and AI-Service Classes have been combined into one GameAI class.
* Testing has been made robust (each vertical row of a grid is checked for victories and imminent victories, more imminent horizontal victories are checked.)
* Fixed a large bug where the AI didn't reset the game board between iterations when comparing columns to drop a piece.
* AI now selects moves that lead to imminent victory.
* AI looks 6 moves ahead (depth 6 for minimax) without noticeable delay when playing.
    * Games against it are on average more difficult to win.

## Problems and Questions

*


## Next Steps

* Improve unit testing to cover more situations.
    * Test that the AI blocks imminent wins for player (3 in a row, later 2 in a row).
* Look into performance/stress testing.


## Hours spent

|Date|Hours spent|Work focus|
|---|---|---|
|8.6.|1|Documentation, refactoring project structure|
|8.6.|2|Testing, refactoring AI code|
|Total hours:|3|
