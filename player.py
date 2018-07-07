#!/usr/bin/python
"""
A base Player object

This player object is used to keep track of the end user
who is playing the game
"""

class Player:
    """
    The player object that will guess what number is rolled
    """
    
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._strikes = 0
        self._score = 0
        self._total_guesses = 0

    def get_whole_name(self):
        """
        Return first and last name concatinated
        """
        return (self.get_first_name() + ' ' + self.get_last_name()).title

    def get_first_name(self):
        """
        Return first name of the player
        """
        return self._first_name

    def get_last_name(self):
        """
        Return last name of the player
        """
        return self._last_name

    def get_strikes(self):
        """
        Return the amount of strikes the player has
        """
        return self._strikes

    def get_score(self):
        """
        Return the amount of points the player has
        """
        return self._score

    def set_first_name(self, new_first_name):
        """
        Assign first name of the player
        """
        self._first_name = new_first_name

    def set_last_name(self, new_last_name):
        """
        Assign last name of the player
        """
        self._last_name = new_last_name

    def add_strikes(self, strikes):
        """
        Add an amount of strikes to the user
        """
        if self.validate_integer(strikes):
            self._strikes += strikes
            print "Incorrect guess. You have " + str(self.get_strikes()) + " strikes!"
            print

    def remove_strikes(self, strikes):
        """
        Remove an amount of strikes from the user
        """
        if self.validate_integer(strikes):
            self._strikes -= strikes
            print "You guessed correctly. You have " + str(self.get_strikes()) + " strikes!"
            print
    
    def add_points(self, new_points):
        """
        Add an amount of points to the player's score
        """
        if self.validate_integer(new_points):
            self._score += new_points

    def remove_points(self, new_points):
        """
        Remove an amount of points from the player's score
        """
        if self.validate_integer(new_points):
            self._score -= new_points

    def get_guesses(self):
        """
        Return the number of guesses the player has for a given round
        """
        return self._total_guesses

    def add_guess(self, guess):
        """
        Add a guess for every dice roll
        """
        self._total_guesses += guess

    def validate_integer(self, new_points):
        """
        Ensures the amounts of points to be added or removed is a positive integer
        """
        if (int(new_points) > 0):
            return True
        else:
            print "Please enter a positive number."
            return False

    def reset_player(self):
        """
        Reset player strikes and score
        """
        self._score = 0
        self._strikes = 0
        self._total_guesses = 0
