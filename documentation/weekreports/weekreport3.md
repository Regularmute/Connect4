# Week 3 (May 29th - June 4th)

## Progress Made

* More unittests have been added for Game service.
* Discovered and fixed a bug where the game wasn't recognizing victories in certain columns. This also affected the AI.
* Decoupled victory checking by calling it from the main game loop instead of inside update_grid.
* AI seems to recognize immediate horizontal and vertical victories.


## Problems and Questions

* I am struggling a bit with the evaluation function: probably I'll have to  define multiple conditions that either add or reduce points from the game state, then return the final adjusted score at the end of the function.
* Currently the AI doesn't stop immediate victories for the player: most likely an issue in tracking which player's turn it is.
* Still haven't done tests for the ai-service yet.


## Next Steps

* Improve the evaluation functions
* Set up tests for AI-service
* Finish draft of testing document

## Hours spent

|Date|Hours spent|Work focus|
|---|---|---|
|29.5.|2|Testing, refactoring, bug fixing|
|Total hours:|2|
