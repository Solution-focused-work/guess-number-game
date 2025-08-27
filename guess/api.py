import random
import csv
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Global to hold game state - in production use a DB or session management
game_state = {
    "player": None,
    "difficulty": None,
    "low": None,
    "high": None,
    "target": None,
    "max_attempts": 10,
    "attempts": 0,
    "game_over": False,
}

def log_result(player: str, difficulty: str, attempts: int, target: int, result: str):
    """Save game result to a CSV file."""
    filename = "game_log.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Player", "Difficulty", "Attempts", "Target", "Result"])
        writer.writerow([player, difficulty, attempts, target, result])

    print(f"✅ Logged: {player}, {difficulty}, {attempts}, {target}, {result}")

def choose_difficulty(level: str) -> tuple[int, int]:
    """Return (low, high) range based on difficulty string."""
    choice = level.strip().lower()
    if choice == "easy":
        return 1, 20
    elif choice == "medium":
        return 1, 50
    elif choice == "hard":
        return 1, 100
    else:
        raise ValueError("Invalid difficulty level. Choose easy, medium, or hard.")

def check_guess(guess: int, target: int) -> str:
    """Check guess against target and return hint."""
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"


@app.route('/start', methods=['POST'])
def start_game():
    data = request.json
    player_name = data.get('player', 'Anonymous')
    difficulty = data.get('difficulty', 'medium')

    try:
        low, high = choose_difficulty(difficulty)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    target = random.randint(low, high)
    game_state.update({
        "player": player_name,
        "difficulty": difficulty,
        "low": low,
        "high": high,
        "target": target,
        "attempts": 0,
        "game_over": False,
    })

    return jsonify({
        "message": f"Game started for {player_name} - guess a number between {low} and {high}",
        "max_attempts": game_state["max_attempts"]
    })


@app.route('/guess', methods=['POST'])
def guess():
    if game_state["game_over"]:
        return jsonify({"error": "Game is over. Please start a new game."}), 400

    data = request.json
    guess = data.get("guess")
    if guess is None or not isinstance(guess, int):
        return jsonify({"error": "Please provide an integer 'guess' in the JSON body."}), 400

    result = check_guess(guess, game_state["target"])
    game_state["attempts"] += 1

    if result == "Correct!":
        game_state["game_over"] = True
        log_result(
            game_state["player"], 
            f"{game_state['low']}-{game_state['high']}", 
            game_state["attempts"], 
            game_state["target"], 
            "Win"
        )
        return jsonify({
            "result": result,
            "attempts": game_state["attempts"],
            "message": f"🎉 You guessed it in {game_state['attempts']} attempts!"
        })

    if game_state["attempts"] >= game_state["max_attempts"]:
        game_state["game_over"] = True
        log_result(
            game_state["player"], 
            f"{game_state['low']}-{game_state['high']}", 
            game_state["attempts"], 
            game_state["target"], 
            "Loss"
        )
        return jsonify({
            "result": "Game over! The correct number was " + str(game_state["target"]),
            "attempts": game_state["attempts"]
        })

    return jsonify({
        "result": result,
        "attempts": game_state["attempts"],
        "attempts_left": game_state["max_attempts"] - game_state["attempts"]
    })


if __name__ == "__main__":
    app.run(debug=True)
