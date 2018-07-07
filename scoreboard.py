"""
A base scoreboard object

This is a scoreboard object which is to keep
stats while the game is running. If the game
exists, all statistics are lost.
"""

class Scoreboard:
    """
    The scoreboard object will keep historical scoring temporarily
    """

    def __init__(self):
        self._scoreboard = []

    def get_scoreboard(self):
        """
        Returns the scoreboard object (a list of dictionaries).
        """
        return self._scoreboard

    def append_round(self, round_number, whole_name, score, total_strikes):
        """
        Appends a round of Dice Game to the scoreboard
        """
        self._scoreboard.append({
            "Round": round_number,
            "Player Name": whole_name,
            "Score": score,
            "Total Strikes": total_strikes
        })

    def print_scoreboard(self):
        """
        Prints scoreboard object with formatting
        """
        scoreboard = self.get_scoreboard()

        print "Round Stats:"
        print "************"
        for game_round in scoreboard:
            print "Round: " + str(game_round['Round']).rjust(1),
            print "Score: " + str(game_round['Score']).rjust(2),
            print "Total Guesses: " + str(game_round['Total Strikes']).rjust(1),
            print "Name: " + str(game_round['Player Name']).rjust(1)
