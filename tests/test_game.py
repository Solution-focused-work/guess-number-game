import pytest
from unittest.mock import patch, mock_open
from guess.game import check_guess, log_result, play_game


# ✅ Simple logic test — no I/O
def test_check_guess_correct():
    assert check_guess(5, 5) == "Correct!"


def test_check_guess_low():
    assert check_guess(3, 5) == "Too low!"


def test_check_guess_high():
    assert check_guess(7, 5) == "Too high!"


# ✅ Test logging to CSV
@patch("builtins.open", new_callable=mock_open)
@patch("os.path.isfile", return_value=False)
def test_log_result(mock_exists, mock_file):
    log_result("TestPlayer", "1-20", 3, 15, "Win")
    handle = mock_file()
    handle.write.assert_called()  # Check that write was called


# ✅ Test the game logic with controlled input/output
@patch("random.randint", return_value=7)
@patch("builtins.input", side_effect=["easy", "7"])  # difficulty, then guess
def test_play_game_win(mock_input, mock_randint):
    result = play_game("Tester", max_attempts=5)
    assert result is True
