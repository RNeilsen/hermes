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

