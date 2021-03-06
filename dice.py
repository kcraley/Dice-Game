"""
Dice Game

The objective of this game is to guess the correct
number that is going to be rolled. The player starts
with zero strikes. If the player guesses the number
within two numbers a strike is added. When three
strikes are reached the game is over.
"""

def main():
    """
    The main method for running Dice Game
    """
    from player import Player
    from game import Game
    from scoreboard import Scoreboard

    # Instantiate game
    dice_game = Game()

    # Instantiate scoreboard
    scoreboard = Scoreboard()

    # Get Player's name and instantiate
    first_name, last_name = dice_game.prompt_user_name()
    user = Player(first_name, last_name)

    # Prompt Player with instructions
    dice_game.welcome_prompt(user.get_whole_name())

    # Declare global variables
    round_number = 1
    play_again = True
    correct = 0

    # Main game loop
    while play_again:
        # Obtain the Player guess
        guess = dice_game.get_user_guess()
        user.add_guess(1)

        # Roll the dice
        dice_roll = dice_game.roll_dice()

        # Verify guesses from the user
        if guess != dice_roll:
            user.add_strikes(1)
            correct = 0
        elif guess == dice_roll:
            correct += 1
            if correct >= 2:
                user.remove_strikes(2)
                user.add_points(int(25 + (25 * 0.5 + correct)))
            else:
                user.remove_strikes(1)
                user.add_points(25)

        # Play again if the Player gets 3 or more strikes?
        if user.get_strikes() >= 3:
            scoreboard.append_round(round_number,
                                    user.get_whole_name(),
                                    user.get_score(),
                                    user.get_guesses())
            round_number += 1
            user.reset_player()
            play_again = dice_game.play_again()

    scoreboard.print_scoreboard()

if __name__ == '__main__':
    main()
