
# Libraries
import random

# Functions
def play(time: float, player: dict) -> None:
    """
    Plays the game of chance.

    The game of chance is a simple game where the player either wins or loses a
    coin at random. The probability of winning is 0.5.

    Parameters
    ----------
    time : float
        The current time.
    player : dict
        The player's state as a dictionary.

    Returns
    -------
    None
    """
    if random.random() < 0.5:
        player["money"] += 1
        print("You won a coin!")
    else:
        player["money"] -= 1
        print("You lost a coin!")

    time += 1
