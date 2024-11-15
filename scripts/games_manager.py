
# Libraries
import os

# Functions
def load_games() -> dict:
    """
    Loads all games from the `games` directory.

    This function iterates over all .py files in the `games` directory and
    imports the `play` function from each module, storing it in a dictionary
    with the module name as the key.

    Returns:
        dict: A dictionary mapping game names to play functions.
    """
    games = {}

    for file in os.listdir("games"):
        if file.endswith(".py") and file != "__init__.py":
            module_name = file[:-3]
            module = __import__("games." + module_name, fromlist=[module_name])
            games[module_name] = module.play

    return games

if __name__ == "__main__":
    print(load_games())
