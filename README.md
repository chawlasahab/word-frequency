# word-frequency
## Description
Program to fetch a wikipedia page and report top n words on that.

## Requirements:
* python3

## Setup:
To install dependencies.
* `make install`

## Unit-Tests:
To run unit-tests.
* `make test`

## Instructions
One command execution, includes dependencies installation, flake8 check, unit-tests execution and program execution:

For custom pageid and top n words, use below command:
* `make run pageid=PAGEID n=N` (example: `make run pageid=21721040 n=5`)

For default execution, use below command:
* `make default`