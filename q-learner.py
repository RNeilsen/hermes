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

       :observation: An observation of the game observation
       :returns: pandas Series

       """
       pass

    def update(self, before_observation, move, after_observation, reward):
        """Update the Q matrixs to take account of the new information.

        :before_observation: before-move observation
        :move: the move taken
        :after_observation: after-move observation
        :reward: the reward the game offers
        :returns: None

        """
        pass


class QLearner(object):

    """A class implementing a q-learner
    See https://en.wikipedia.org/wiki/Q-learning
    """

    def __init__(self, game, qmatrix=None, randomness=1):
        """Initialize the class.
        :qmatrix: A QMatrix instance.
        :game: An instance of a Game
        :randomness: A scaling factor > 0 indicating how likely less
                     than optimal moves will be made
                     (encourages exploration)
        :returns: None"""
        self._Q = QMatrix() if qmatrix is None else qmatrix
        self._randomness = 1
        self._game = game
        self._latest_move = None
        self._latest_observation = None

    def select_move(self, observation, available_moves):
        """Select the next move to make somewhat randomly.

        :observation: an observation of the observation of the game
        :available_moves: list of possible actions which can be made
        :returns: The move selected to be made

        """
        rewards = self._Q[observation]
        # Softmax weights
        selection_weights = np.exp(rewards / self._randomness)
        move = random.choices(
            population=rewards.index,
            weights=selection_weights,
            k=1)[0]
        assert move in available_moves, 'Invalid move selected'
        return move

    def _make_move(self, move):
        """Make a move in the game, and record the previous move, and the current observation

        :move: a move that can be made
        :returns: reward from the game

        """
        reward = self._game.make_move(move)
        return reward


    def _serialize_observation(self, observation):
        """serialize the observation for storage in the QMatrix
        :observation: the state of a game
        :returns: string

        """
        # Should this be part of game?
        pass

    def step(self):
        """Iterate a turn of the game
        :returns: None. Updates the Q matrix

        """
        observation = self._serialize_observation(
            self._game.get_cur_state()
        )
        # We can't update our Q until it's our turn again
        self._Q.update(self._latest_observation,
                       self._latest_move,
                       observation,
                       self._latest_reward)

        move = self._select_move(observation, available_moves)

        self._latest_reward = self.make_move(move)
        self._latest_observation = observation
        self._latest_move = move

