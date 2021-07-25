import random

class RandomPlayer(object):

    """A player that just makes random moves in the game"""

    def __init__(self):
        """ """
        pass

    def select_move(self, observation, available_moves):
        """Selects a move at random from available_moves

        :observation: observation of the game
        :available_moves: moves that could be made
        :returns: move to make

        """
        return random.choice(available_moves)

    def update_score(self, *args):
        """TODO: Updates the random_player's score. Ignored

        :*args: arguments
        :returns: None

        """
        pass

