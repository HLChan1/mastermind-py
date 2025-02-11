# Mastermind Game

This is a simple implementation of the classic Mastermind game with a graphical user interface.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)

## Installation

To run this project, you need to have Python installed on your machine. You can install the required dependencies using pip. Run the following command in your terminal:

```
pip install -r requirements.txt
```

## Usage

To start the game, run the main Python file:

```
python src/main.py
```

This will initialize the graphical user interface and start the game loop.

## Game Rules

Mastermind is a code-breaking game for two players. One player (the codemaker) selects a secret code, and the other player (the codebreaker) tries to guess it within a certain number of attempts.

1. The code consists of a sequence of colors (or numbers) chosen from a set.
2. After each guess, the codemaker provides feedback in the form of black and white pegs:
   - A black peg indicates a correct color in the correct position.
   - A white peg indicates a correct color in the wrong position.
3. The game continues until the codebreaker guesses the code or runs out of attempts.

Enjoy playing!