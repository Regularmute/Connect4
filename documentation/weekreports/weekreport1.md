# Week 1 (May 15th - May 21st)

## Progress Made

* Project has been created
* Git repository/Version control initialized
* Empty grid is initialized and user can drop pieces into columns.

This week I have settled on the subject of my project and a loose idea on how to execute it. I have set up the git repository and virtual environment for the project, along with some documentation. I have also learned about minimax and alpha-beta pruning.

## Problems and Questions

* Currently I am thinking of displaying the game board as a list of lists, where each list represents a row, and each index in a row represents a tile. Is this a bad idea?
* I struggled a bit to understand Transposition Tables in the latter part of the minimax.pdf. I believe I will figure it out, it seems that there are two ways to keep track of one: by creating a new hash table everytime the AI makes a move, or by updating one table over the course of the entire game through Zobrist hashing?

## Next Steps

* I believe implementing the actual game so that a human player can play against an AI with random moves is a good start. This way I can check that the actual game works, making it easier to develop the more sophisticated AI.
* Begin implementing the minimax algorithm with a depth of one.
* Figure out how transposition tables work and what is Zobrist hashing.

## Hours spent

|Date|Hours spent|Work focus|
|---|---|---|
|18.5.|2|Studying MinMax and Alpha-beta|
|18.5.|3|Documentation: project specification, git-repo|
|19.5.|1|Documentation|
|19.5.|1|Project initialization|
|Total hours:|7|
