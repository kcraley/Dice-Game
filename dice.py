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

    dice_game = Game()

    first_name, last_name = dice_game.prompt_user_name()
    user = Player(first_name, last_name)

    dice_game.welcome_prompt(user)

    play_again = True
    while play_again:
        guess = dice_game.get_user_guess()
        dice_roll = dice_game.roll_dice()

        if guess != dice_roll:
            user.add_strikes(1)
        elif guess == dice_roll:
            user.remove_strikes(1)
        if user.get_strikes() >= 3:
            play_again = dice_game.play_again(user)

if __name__ == '__main__':
    main()