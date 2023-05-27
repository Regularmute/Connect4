# Week 2 (May 22nd - May 28th)

## Progress Made

* Unittests have been made for UI, game logic and integration tests have been made for them.
* Test branch coverage reports can be made and viewed.
* Pylint has been implemented to check code.
* The game checks for victory after every move.
* Game logic and UI have been separated into modules.
* Added a computer opponent who drops pieces randomly.
* Begin implementing minimax-algorithm for the AI.


This week I have begun testing, and learned how to check for console outputs in testing as well with StringIO. I also received good practice with modularizing code from one file to multiple.

I've also grown more familiar with minimax through trying to implement it, and the necessary supplementary functions to call it in the first place, and to evaluate the game state. This has required experimenting with different heuristics for optimal Connect 4 gameplay.

## Problems and Questions

Currently the AI doesn't seem to recognize horizontal wins. I also struggle with figuring out how to write tests for the AI class. Implementing the column/move choosing function is also difficult, minimax algorithm seems to be doable with the course material's pseudocode.

I am still trying to figure out the best way to transmit information through recursion about last moves etc.

Plan is to first make the AI seem somewhat intelligent through brute force, then fixing the code.

## Next Steps

Improve the column-selecting function and confirm that the minimax function works at depth 3 or 4.

Following that, I will attempt to improve the depth of the minimax searching through heuristics, such as affecting the order of game states to be explored, and eventually switching to iterative deepening, where instead of a flat depth for the search, the algorithm checks how much time it "has left" on each level of searching before deciding to stop running or to search one level deeper.

## Hours spent

|Date|Hours spent|Work focus|
|---|---|---|
|22.5.|1|Setting up tests|
|22.5.|1|Docstring, errors, victory checking|
|24.5.|3|Testing, refactoring code|
|25.5.|2|Testing, modularization|
|26.5.|4|Minimax, AI, game state evaluation, styling|
|27.5.|1|Documentation|
|Total hours:|12|
