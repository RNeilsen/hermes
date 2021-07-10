"""
A class implementing a q-learner
https://en.wikipedia.org/wiki/Q-learning
"""
import pandas as pd
import numpy as np
import random

class QMatrix(object):

    """An object containing the current Q matrix as understood by a Q learner.
    """

    def __init__(self):
        self._Q = pd.DataFrame()

   def __get__(self, observation):
       """Get the collection of moves the Q-learner could make, and the
          expected return from them. It will still return something even
          if it has never recorded this observation before.

       :observation: An observation of the game state
       :returns: pandas Series

       """
       pass

    def __set__(self, observation, move):
        """Update the Q matrixs to take account of the new information.

        :observation: TODO
        :move: the move taken
        :returns: None

        """
        pass

class QLearner(object):

    """A class implementing a q-learner
    See https://en.wikipedia.org/wiki/Q-learning
    """

    def __init__(self, qmatrix=None, randomness=1):
        """Initialize the class.
        :qmatrix: A QMatrix instance.
        :randomness: A scaling factor > 0 indicating how likely less
                     than optimal moves will be made
                     (encourages exploration)
        :returns: None"""
        self._Q = QMatrix() if qmatrix is None else qmatrix
        self._randomness = 1

    def _select_move(self, observation):
        """Select the next move to make somewhat randomly.

        :observation: an observation of the state of the game
        :returns: The move selected to be made

        """
        rewards = self._Q[observation]
        # Softmax weights
        selection_weights = np.exp(rewards / self._randomness) 
        move = random.choices(
            population=rewards.index,
            weights=selection_weights,
            k=1)[0]
        return move

