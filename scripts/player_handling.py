
# Libraries
import json
import os

# Constants
SAVE_PATH = "C:/ProgramData/ccasino-saves/latest.json"
START_DATA = {
    "money": 0,
    "days": 0,
}

# Variables
player: dict = {}

# Functions
def load_playerstate() -> dict:
    """
    Loads the player's state from a JSON file.

    Returns:
        dict: The player's state as a dictionary. If the file does not exist, returns an empty dictionary.
    """
    try:
        f = open(SAVE_PATH)
    except FileNotFoundError:
        return {}
    data = json.load(f)
    f.close()
    return data

def save_playerstate():
    """
    Saves the current player's state to a JSON file located at SAVE_PATH.

    If the directory does not exist, it will be created.

    Raises:
        FileNotFoundError: If the file cannot be opened for writing.
    """
    try:
        f = open(SAVE_PATH, "w")
    except FileNotFoundError:
        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
        f = open(SAVE_PATH, "w")
    data = player.copy()
    json.dump(data, f)
    f.close()

def init_player():
    """
    Initializes the global player variable with the player's state.

    Loads the player's state from a JSON file using `load_playerstate()`. If the
    player state is not found (i.e., the file does not exist), initializes the
    player state with a default START_DATA.

    The initialized player state is stored in the global variable `player`.
    """
    global player
    data = load_playerstate()
    if data == {}:
        data = START_DATA
    player = data

def reset_playerstate():
    """
    Resets the player's state by deleting the JSON file located at SAVE_PATH.

    Raises:
        FileNotFoundError: If the file cannot be deleted.
    """
    try:
        os.remove(SAVE_PATH)
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    reset_playerstate()
