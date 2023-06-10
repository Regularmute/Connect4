# Week 4 (June 5th - June 11th)

## Progress Made

* GameService and AI-Service Classes have been combined into one GameAI class.
* Testing has been made robust (each vertical row of a grid is checked for victories and imminent victories, more imminent horizontal victories are checked.)
* Fixed a large bug where the AI didn't reset the game board between iterations when comparing columns to drop a piece.
    * The same bug was found inside the minimax functions.
* AI now selects moves that lead to imminent victory.
* AI now prevents imminent victories by player.
* AI now searches for moves in the middle columns before moving onto outer columns. It feels like games after this change have become significantly harder for the player to win.

* Performance testing the duration of AI's move selection has been started.

## Problems and Questions

* Currently I'm not sure how to go about performance or stress testing the project, I will most likely look at the course material for Java and try to apply some principles for Python. In addition, I will most likely search online for information as well.
    * What would be some good ways to performance test this project? I have currently tried to track the amount of time taken by the AI to choose a move with different depths. Perhaps after implementing the iterative deepening in the future, I can try to calculate something related to that as well?
    * I've been reading up on [this example](https://github.com/TiraLabra/Testing-and-rmq/tree/master/src/main/java/rmq/util) and don't quite understand if measuring preprocessing time is applicable in my project, since the input never scales. The only scaling variable seems to be the depth of the minimax-algorithm's calculation.


## Next Steps

* Improve unit testing to cover more situations.
    * Test that the AI blocks imminent wins for player (3 in a row, later 2 in a row).
* Look into performance/stress testing.


## Hours spent

|Date|Hours spent|Work focus|
|---|---|---|
|8.6.|1|Documentation, refactoring project structure|
|8.6.|2|Testing, refactoring AI code|
|9.6.|2|Testing, refactoring Minimax|
|10.6.|1|Performance testing, documentation, code refactoring|
|Total hours:|6|
