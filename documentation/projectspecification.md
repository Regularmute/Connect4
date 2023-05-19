# Project Specification

The Connect4-application should provide a competent AI opponent to play [Connect 4](https://en.wikipedia.org/wiki/Connect_Four) on a 7-column-wide and 6-row-high grid. If development proceeds faster than expected, it's possible to consider enabling games of Connect 4 played by two AIs against each other. The AI will be developed with the minimax-algortihm enhanced with alpha-beta pruning.

Depending on the achieved depth, the AI should win more often as the amount of moves it looks ahead increases. Furthermore the AI should select its moves relatively quickly.

We will attempt to develop the algorithm with iterative deepening depth-first-search, where the algorithm looks ahead as many moves as possible in a certain amount of time.

The project will be written in Python, and documentation will be written in English for consistency.

The developer is participating in Helsinki University's Computer Science degree (Tietojenkäsittelytieteen Kandiohjelma, TKT).

## Inputs and outputs

### Input:
On their turns, the player will be prompted to enter their move in the console, possibly as a number matching the column where the piece will be droppes. The game board is then updated by switching the lowest tile in the input column from an empty space (".") to the player piece ("X").

Another possibility is to provide the player with the option of selecting the difficulty of AI when starting a game, which would increase or decrease the depth of the minimax algorithm.

### Output:
The game board will be visually represented in the console through ASCII and updated after every move. The board is displayed as 6 rows with 7 characters each, where "." stands for an empty space, "X" stands for a space occupied by the player's piece and "O" stands for a space occupied by the AI's piece.

In the below example the player moved first, and both players simply kept piling their piece on top of their previous one:

```
.......
.......
...X...
...XO..
...XO..
...XO..
```


## Algorithms and Data Structures

The main focus of this project will be developing a  minimax-algorithm, and improving it with alpha-beta pruning. These algorithms will treat game states as nodes in a tree, with edges between one game state and another reached with one move. The root node is the game's current state at the time of the algorithm's execution.

The program will use a transposition table to store information on how various moves affect the game state and speed up the algorithm. We may possibly use hash tables or Zobrist hashing to implement the transposition table depending on if we want to keep track of previous moves made during the game.

## Target Time and Space Complexities

According to the course material, minimax-algorithm has a time complexity of $O^n$, where $O$ is the amount of available moves in a game situation, and $n$ is the depth of moves the algorithm looks ahead to. Since we use 7 columns in our game of Connect 4, there are always 7 options for a player to drop a piece, barring any filled columns. This means that worst case time-complexity for our minimax algorithm will be $O(7^n)$, where $n$ is the amount of moves our algorithm looks ahead.

However, we will be enhancing the algorithm with alpha-beta pruning, which if implemented correctly should reduce the runtime to $O(7^{n/2})$. Therefore the time complexity remains exponential, but enables an increased depth of 1-2 moves further than with pure minimax.

As the minimax-algorithm will use iterative deepening depth-first search for each branch, and according to wikipedia IDDFS has a space complexity of $O(d)$, where $d$ is the depth of the search and $b$ is the amount of branches to search at each node, our target space complexity is $O(bd)$. Our AI will have 7 moves to evaluate most of the time, so the target space complexity can be represented as $O(7d)$.



## Sources:

* Course material for minimax: https://tiralabra.github.io/2023_alkukesa/fi/aiheet/minimax.pdf
* Wikipedia articles:
    * https://en.wikipedia.org/wiki/Minimax
    * https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    * https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search
