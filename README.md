# 🎯 Number Guessing Game

A simple **Python-based CLI game** where the computer randomly selects a number, and the player tries to guess it within limited attempts.  
Difficulty levels (easy, medium, hard) change the range of numbers. The game also logs results to a CSV file.

---

## 🚀 Features
- Choose difficulty:
  - Easy → number between 1–20
  - Medium → number between 1–50
  - Hard → number between 1–100
- Limited attempts (default: 10).
- Validates user input.
- Keeps track of wins/losses.
- Logs results to `game_log.csv`.

---

## 🖥️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   cd number-guessing-game

---

## 🎮 Example Gameplay

Enter your name: Alice
Choose difficulty (easy / medium / hard): easy
🎯 Welcome to Number Guessing Game, Alice!
You have only 10 attempts to guess the number between 1 and 20.

Enter your guess 1-20: 10
Too low!
Attempts left: 9

Enter your guess 1-20: 15
Too high!
Attempts left: 8

Enter your guess 1-20: 13
🎉 You guessed it in 3 attempts.

✅ Logged: Alice, easy, 3, 13, Win

