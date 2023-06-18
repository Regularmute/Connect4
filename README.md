# Connect4

This project is part of Helsinki University's Data Structures Project course.

## Testing coverage

The test branch coverage report can be seen in the testing document: [Testing Document](https://github.com/Regularmute/Connect4/blob/main/documentation/testingdocument.md)

## Documentation links

* [Project specification document](https://github.com/Regularmute/Connect4/blob/main/documentation/projectspecification.md)
* [Testing document](https://github.com/Regularmute/Connect4/blob/main/documentation/testingdocument.md)
* [Implementation document](https://github.com/Regularmute/Connect4/blob/main/documentation/implementationdoc.md)
* Weekly reports:
    * [Week 1](https://github.com/Regularmute/Connect4/blob/main/documentation/weekreports/weekreport1.md)
    * [Week 2](https://github.com/Regularmute/Connect4/blob/main/documentation/weekreports/weekreport2.md)
    * [Week 3](https://github.com/Regularmute/Connect4/blob/main/documentation/weekreports/weekreport3.md)
    * [Week 4](https://github.com/Regularmute/Connect4/blob/main/documentation/weekreports/weekreport4.md)
    * [Week 5](https://github.com/Regularmute/Connect4/blob/main/documentation/weekreports/weekreport5.md)

## Installation instructions

Note: The project uses [Poetry](https://python-poetry.org/), and the poetry commands may not work correctly on Windows operating systems. In case the poetry invoke commands don't work, use the corresponding commands written in the [tasks.py](https://github.com/Regularmute/Connect4/blob/main/tasks.py) file. E.g. instead of 'poetry run invoke test', type 'pytest src' in the console.

1. Clone the repository to your computer.
2. Navigate to the repository's root directory, then install dependencies for poetry with
´poetry install´
3. Run the game with
´poetry run invoke start´

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
