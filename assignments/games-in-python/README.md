
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game that uses Python strings, loops, conditionals, and user input. Practice tracking game state while revealing a randomly selected word one letter at a time.

## 📝 Tasks

### 🛠️ Build the Word and Guessing Logic

#### Description
Create the logic for choosing a secret word and displaying the letters the player has guessed correctly.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list.
- Accept a letter guess from the player.
- Display the current word progress, showing unguessed letters as underscores (for example, `_ _ _`).
- Reveal every matching position when a guessed letter appears more than once in the word.

### 🛠️ Run and End the Game

#### Description
Add a game loop that tracks incorrect guesses and ends with the appropriate result when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Track and display how many incorrect guesses remain.
- Continue prompting for guesses until the word is guessed or no attempts remain.
- Display a win message when the player guesses the word.
- Display a lose message and reveal the secret word when attempts are exhausted.
