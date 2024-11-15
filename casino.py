
# Libraries
import pyfiglet
import sys
import scripts.player_handling as ph
import scripts.games_manager as gm

# Functions
def enter_app() -> None:
    """
    Initializes the player and starts the game loop.

    This function is the entry point of the application. It initializes the
    player's state using `scripts.player_handling.init_player()` and then enters
    the game loop using `game_loop()`.
    """
    ph.init_player()

    game_loop()
    ph.init_player()

    game_loop()

def exit_app() -> None:
    """
    Exits the application.

    This function saves the current player state using
    `scripts.player_handling.save_playerstate()` and then exits the application
    using `sys.exit(0)`.
    """
    print("Saving player state...")
    ph.save_playerstate()

    print("\nExiting app...")
    sys.exit(0)

def welcome() -> None:
    """
    Prints a welcome message to the user.

    This function prints a welcome message to the user using the `pyfiglet`
    library. The message is formatted with the "slant" font and has a width of
    1000 characters.
    """
    print(pyfiglet.figlet_format("WELCOME TO THE CASINO", font="slant", width=1000))

def game_loop() -> None:
    """
    Main loop of the casino game.

    This function represents the main loop of the game, where each iteration
    corresponds to a new day in the game. It updates the player's state for
    the new day using `day_update()` and then manages the day's activities
    with `manage_day()`.
    """
    while True:
        day_update(ph.player)
        manage_day(ph.player)

def day_update(player: dict) -> None:
    """
    Updates the player's state for the new day.

    This function increments the player's "days" counter and prints out the
    new day number. It does not return anything.

    Parameters
    ----------
    player : dict
        The player's state as a dictionary.

    Returns
    -------
    None
    """
    player["days"] += 1
    print(f"\nDay {player['days']}")

def manage_day(player: dict) -> None:
    """
    Manages the activities for the day in the casino game.

    This function prompts the player to decide whether to enter the casino at the start
    of a new day. If the player chooses to enter, it initiates the day's activities by
    repeatedly asking the player to choose an action until they decide to leave or the
    casino closes. The function tracks the time spent in the casino and handles the exit
    process, saving the player's state if necessary.

    Parameters
    ----------
    player : dict
        The player's state as a dictionary.

    Returns
    -------
    None
    """
    while True:
        entering = input("\nA new day has begun. Do you want to enter the casino? (y/n) ").lower()
        if entering == "y":
            welcome()
            break
        elif entering == "n":
            exit_app()
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    time = 0.0
    while True:
        print(f"\nTime: {time} hours")
        action = choose_activity()
        print()
        time, player = get_actions()[action](time, player)
        match action:
            case "leave": break

        if time >= 24:
            print("\nThe casino is closed now.")
            leave_casino(time, player)
            break

    print("\nYou have reached the end of the day. Time to sleep. Good night!")

def choose_activity() -> str:
    """
    Prompts the player to choose an activity from available actions.

    This function continuously displays a list of available actions and prompts
    the player for input until a valid action is selected. The function returns
    the chosen action as a lowercase string.

    Returns
    -------
    str
        The name of the chosen action.
    """
    actions = get_actions().keys()

    while True:
        for action in actions:
            print("- " + action)
        action = input("What do you want to do? ").lower()

        if action in actions:
            return action
        else:
            print("Invalid input. Please enter a valid action.")

def get_actions() -> dict:
    """
    Returns a dictionary of available actions in the casino.

    The returned dictionary maps action names to the corresponding functions
    that implement the actions. The functions take two arguments: the current
    time and the player's state.

    Returns
    -------
    dict
        A dictionary mapping action names to action functions.
    """
    return {
        "leave": leave_casino,
        "wait": wait,
        "view self": view_player,
        "get rich": get_rich,
        "play game": choose_and_play_game,
    }

def leave_casino(time: float, player) -> tuple[float, dict]:
    """
    Leaves the casino and saves the player's state.

    Prints a message indicating that the player has left the casino and then
    saves the player's state using `scripts.player_handling.save_playerstate()`.
    The function does not modify the player's state in any other way and
    returns the current time and the player's state unchanged.

    Parameters
    ----------
    time : float
        The current time.
    player : dict
        The player's state as a dictionary.

    Returns
    -------
    tuple[float, dict]
        A tuple containing the current time and the player's state.
    """
    print("You left the casino.")

    print("Saving player state...")
    ph.save_playerstate()

    return time, player

def wait(time: float, player) -> tuple[float, dict]:
    """
    Waits for a specified number of hours.

    Prompts the user to enter the number of hours to wait and checks for valid
    input. If the input is valid, prints a message indicating that the player
    waited for the given number of hours and updates the current time
    accordingly. The function does not modify the player's state in any other
    way and returns the updated time and the player's state unchanged.

    Parameters
    ----------
    time : float
        The current time.
    player : dict
        The player's state as a dictionary.

    Returns
    -------
    tuple[float, dict]
        A tuple containing the updated time and the player's state.
    """
    while True:
        try:
            wait_time = float(input("How many hours do you want to wait? "))
            if 0 <= wait_time <= 24 - time:
                break
        except ValueError:
            pass
        print(f"Invalid input. Please enter a number between 0 and {24 - time}.")

    print(f"You waited for {wait_time} hours.")
    time += wait_time

    return time, player

def view_player(time: float, player) -> tuple[float, dict]:
    """
    Prints an overview of the player's state.

    This function prints out the player's state as a dictionary, with each key
    capitalized and indented. The function does not modify the player's state in
    any way and returns the current time and the player's state unchanged.

    Parameters
    ----------
    time : float
        The current time.
    player : dict
        The player's state as a dictionary.

    Returns
    -------
    tuple[float, dict]
        A tuple containing the current time and the player's state.
    """
    print("Player overview:")
    for key, value in player.items():
        print(f"\t{key.capitalize()}: {value}")

    return time, player

def get_rich(time: float, player) -> tuple[float, dict]:
    """
    Increases the player's money by one.

    This function simply increases the player's money by one and prints a
    message indicating that the player got rich. The function does not modify the
    player's state in any other way and returns the current time and the player's
    state unchanged.

    Parameters
    ----------
    time : float
        The current time.
    player : dict
        The player's state as a dictionary.

    Returns
    -------
    tuple[float, dict]
        A tuple containing the current time and the player's state.
    """
    print("You got rich!")
    ph.player["money"] += 1

    return time, player

def choose_and_play_game(time: float, player) -> tuple[float, dict]:
    """
    Prompts the player to choose a game from available games.

    This function loads all available games from the `games` directory using
    `scripts.games_manager.load_games()`, prints a list of the available games,
    and prompts the player to choose a game by entering a number. The function
    continuously prompts for input until a valid number is entered. The
    function then calls the chosen game with the player's state as an argument
    and returns the current time and the player's state.

    Parameters
    ----------
    time : float
        The current time.
    player : dict
        The player's state as a dictionary.

    Returns
    -------
    tuple[float, dict]
        A tuple containing the current time and the player's state.
    """
    games = gm.load_games()

    print("Choose a game:")
    for game in games:
        print(f"- {game}")

    while True:
        choice = input("Enter your choice: ").lower()

        if choice in games.keys():
            break

        print("Invalid input. Please enter the name of a game.")

    game = games[choice]

    print(f"\nPlaying {choice}")

    game(time, player)

    return time, player

if __name__ == "__main__":
    enter_app()