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

    # Instantiate game
    dice_game = Game()

    # Get Player's name and instantiate
    first_name, last_name = dice_game.prompt_user_name()
    user = Player(first_name, last_name)

    # Prompt Player with instructions
    dice_game.welcome_prompt(user.get_whole_name())

    # Main game loop
    play_again = True
    while play_again:
        # Obtain the Player guess
        guess = dice_game.get_user_guess()

        # Roll the dice
        dice_roll = dice_game.roll_dice()

        # Verify guesses from the user
        if guess != dice_roll:
            user.add_strikes(1)
        elif guess == dice_roll:
            user.remove_strikes(1)

        # Play again if the Player gets 3 or more strikes?
        if user.get_strikes() >= 3:
            play_again = dice_game.play_again(user)

if __name__ == '__main__':
    main()
