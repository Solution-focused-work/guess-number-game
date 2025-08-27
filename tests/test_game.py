import pytest
from guess.api import app, check_guess, log_result, play_game
from unittest.mock import patch, mock_open


# Fixture for Flask test client
@pytest.fixture
def client():
    return app.test_client()

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


# API endpoint tests
def test_api_guess_correct():
    response = client.get("/guess?number=5&target=5")
    assert response.status_code == 200
    assert response.json() == {"result": "Correct!"}


def test_api_guess_low():
    response = client.get("/guess?number=3&target=5")
    assert response.status_code == 200
    assert response.json() == {"result": "Too low!"}


def test_api_guess_high():
    response = client.get("/guess?number=7&target=5")
    assert response.status_code == 200
    assert response.json() == {"result": "Too high!"}


# CLI play_game logic test
@patch("random.randint", return_value=7)
@patch("builtins.input", side_effect=["easy", "7"])
def test_play_game_win(mock_input, mock_randint):
    result = play_game("Tester", max_attempts=5)
    assert result is True
