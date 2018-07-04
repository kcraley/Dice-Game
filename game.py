"""
A based Game object

This game object is used to 
"""

class Game:
    """

    """

    def __init__(self):
        pass

    def prompt_user_name(self):
        """
        Prompt the user for their first and last name
        """
        while True:
            try:
                first, last = raw_input("Enter your first and last name: ").split()
                print
            except ValueError:
                print "Please enter exactly only your first and last name. Try again."
                continue
            else:
                break

        return first, last

    def roll_dice(self):
        """
        Roll the dice and return a number from 1 to 6
        """
        import random

        dice_roll = random.randint(1,6)
        print "The computer rolled a " + str(dice_roll) + "."
        return dice_roll

    def get_user_guess(self):
        """
        Prompt the user for their guess
        """
        while True:
            while True:
                try:
                    user_guess = int(raw_input("Please guess a number from 1 to 6: "))
                    break
                except ValueError:
                    print "The value entered is not a whole number. Try again."
            if self.validate_user_guess(user_guess):
                return user_guess
            else:
                print "The number you entered is not between 1 and 6. Try again."

    def validate_user_guess(self, user_guess):
        """
        Validate the user's guess is within 1 and 6
        """
        if (user_guess < 1) or (user_guess > 6):
            return False
        else:
            return True

    def play_again(self, user):
        print "Game Over!"
        while True:
            play_again = str(raw_input("Would you like to play again? [Y|N]: "))
            print
            if (play_again == "Y") or (play_again == "y"):
                return True
            elif (play_again == "N") or (play_again == "n"):
                return False
            else:
                print "Invalid selection. Try again."

    def welcome_prompt(self, user):
        """
        Show the player the welcome prompt
        """
        print "Dice Game"
        print "*********"
        print "Welcome " + user.get_whole_name() + "!"
        print "You must guess what number the computer is going to roll."
        print "If you guess correctly, you win the game. Otherwise, if"
        print "you guess incorrectly, a strike is given and you can"
        print "continue to guess. If you reach three strikes, the game"
        print "is over. Guessing correctly will remove up to two of your"
        print "strikes. Good luck!"
        print
