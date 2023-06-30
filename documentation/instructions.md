# Instructions

## Installation

Note: The project uses [Poetry](https://python-poetry.org/), and the poetry commands may not work correctly on Windows operating systems. In case the poetry invoke commands don't work, use the corresponding commands written in the [tasks.py](https://github.com/Regularmute/Connect4/blob/main/tasks.py) file. E.g. instead of 'poetry run invoke test', type 'pytest src' in the console.

1. Clone the repository to your computer.
2. Navigate to the repository's root directory, then install dependencies for poetry with
´poetry install´
3. Run the game with
´poetry run invoke start´

## Playing

After beginning a game, you are presented with an empty game grid with '0's representing empty tiles, '1's representing your pieces and '2's representing the AI's pieces.

You are prompted to choose a column to drop your piece in by entering an integer between 1 and 7. An inappropriate input will prompt you to try again.

After dropping a piece, the minimax algorithm will begin running and printing how much time it is taking. The algorithm begins at depth 4 and will repeat itself as many times as it can under its time limit.

## Testing

You can run the unit tests with
´poetry run invoke test´

A coverage report can be generated in html form with
´poetry run invoke coverage-report´

You can run performance tests with
´poetry run invoke test-performance´

## Linting

You can run the pylint style checker with
´poetry run invoke lint´
