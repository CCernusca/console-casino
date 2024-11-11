
# Libraries
import json
import os

# Constants
SAVE_PATH = "C:/ProgramData/ccasino-saves/latest.json"
START_DATA = {
    "money": 0
}

# Variables
player: dict|None = None

# Functions
def load_playerstate() -> dict|None:
    """
    Loads the player's state from a JSON file located at SAVE_PATH.

    Returns:
        dict: A dictionary containing the player's state if the file exists.
        None: If the file does not exist.
    """
    try:
        f = open(SAVE_PATH)
    except FileNotFoundError:
        return None
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
    if data is None:
        data = START_DATA
    player = data

if __name__ == "__main__":
    init_player()
    print(player)
    save_playerstate()
