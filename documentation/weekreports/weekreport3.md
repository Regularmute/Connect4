# Week 3 (May 29th - June 4th)

## Progress Made

* More unittests have been added for Game service.
* Discovered and fixed a bug where the game wasn't recognizing victories in certain columns. This also affected the AI.
* Decoupled victory checking by calling it from the main game loop instead of inside update_grid.
* AI seems to recognize immediate victories.
* Revised older minimax algorithm material with a better understanding after some experience with applying it.

I have a more thorough understanding about the minimax algorithm and alpha-beta pruning. I understand each step a bit more thoroughly, and feel like I'm getting closer to implementing it correctly.

I have also learned to perform larger-scale refactoring on the game service code to fit with newly discovered requirements (such as keeping track of the latest move). Furthermore, I have gotten to practice breaking large changes down into separate, clear, legible commits. This practice also helps me stay on top of what kind of changes I actually made during a longer coding session.

As my understanding on the topic has been improving, I also feel more confident about possible unit tests for the AI, though I think I'll have to import the game service for the tests, which might qualify them as integration tests?


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
|1.6.|2|Studying minimax, cleaning code, bug fixing, refactoring minimax|
|Total hours:|2|
