import random
import csv
import os


def choose_difficulty() -> tuple[int, int]:
    """Ask user to choose difficulty level and return (low, high) range."""
    while True:
        choice = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        if choice == "easy":
            return 1, 20
        elif choice == "medium":
            return 1, 50
        elif choice == "hard":
            return 1, 100
        else:
            print("❌ Invalid choice! Please type easy, medium, or hard.")


def get_user_guess(low: int, high: int) -> int:
    """Prompt user for a number within the range [low, high]."""
    while True:
        try:
            guess = int(input(f"Enter your guess {low}-{high}: "))
            if low <= guess <= high:
                return guess
            else:
                print(
                    f"❌ Invalid input! Please enter a number between {low} and {high}."
                )
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def check_guess(guess: int, target: int) -> str:
    """Check guess against target and return hint."""
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"


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


def play_game(player: str, max_attempts=10):
    """Main game loop."""
    low, high = choose_difficulty()
    target = random.randint(low, high)
    attempts = 0

    print(f"🎯 Welcome to Number Guessing Game, {player}!")
    print(
        f"You have only {max_attempts} attempts to guess the number between {low} and {high}."
    )

    while attempts < max_attempts:
        guess = get_user_guess(low, high)
        attempts += 1
        result = check_guess(guess, target)
        print(result)
        if result == "Correct!":
            print(f"🎉 You guessed it in {attempts} attempts.")
            log_result(player, f"{low}-{high}", attempts, target, "Win")
            return True  # Return True to indicate a win
        else:
            print(f"Attempts left: {max_attempts - attempts}")

    # After loop ends without guessing correctly
    print(f"💀 Game over! The correct number was {target}.")
    log_result(player, f"{low}-{high}", attempts, target, "Loss")
    return False  # Return False to indicate a loss


def main():
    """Main entry point to handle replay."""

    player_name = input("Enter your name: ").strip() or "Anonymous"

    wins = 0
    losses = 0

    while True:
        result = play_game(player_name)
        if result:
            wins += 1
        else:
            losses += 1

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n📊 Final Scoreboard:")
            print(f"✅ Wins: {wins}")
            print(f"❌ Losses: {losses}")
            print("👋 Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
