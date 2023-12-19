# Battleships Project

This is a project aimed to develop skills in test driven development and programming terminal user-interfaces.

- The game is played with two people in the terminal, with prompts to direct which player's turn it is.
- First each player places their ships on the game board.
- Then the players take turns firing at the opposition board.
- The winner is the first to sink all of their opponents ships.

## Getting Started

How to get started:

```shell
; pipenv install # To install dependencies

; pipenv run pytest # All tests should pass
; pipenv run pytest --cov lib # To see test coverage too

; pipenv run python run.py
# This will give you a few prompts and show you a board.
```

## User Stories

Here is the full set of user stories for this game.

```
As a player
So that I can prepare for the game
I would like to place a ship in a board location

As a player
So that I can play a more interesting game
I would like to have a range of ship sizes to choose from

As a player
So the game is more fun to play
I would like a nice command line interface that lets me enter ship positions and
shots using commands.

As a player
So that I can create a layout of ships to outwit my opponent
I would like to be able to choose the directions my ships face in

As a player
So that I can have a coherent game
I would like ships to be constrained to be on the board

As a player
So that I can have a coherent game
I would like ships to be constrained not to overlap

As a player
So that I can win the game
I would like to be able to fire at my opponent's board

As a player
So that I know when to finish playing
I would like to know when I have won or lost

As a player
So that I can consider my next shot
I would like to be able to see my hits and misses so far

As a player
So that I can play against a human opponent
I would like to play a two-player game
```
