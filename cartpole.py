"""
Defines the cartpole game. A cart sits on a track, with a pole
standing vertically. The AI can nudge the cart left and right down the
track and is rewarded each timestep for keeping the pole upright

       |
      /
    __|__
===o=====o===

"""
import numpy as np

class CartPole(Game):

    """Cartpole"""

    def __init__(self):
        """Initializes the cartpole game """
        Game.__init__(self, pos, vel, angle, time_step=None)
        self._pos = pos # position of the centre of the cart
        self._vel = vel # the velocity of the cart
        self._angle = angle # angle of the pole relative to vertical in radian
        self._ang_vel = 0 # angular velocity of the pole relative in radian
        self._game_over = False
        self._time_step = 1 if time_step is None else time_step

    def get_cur_state(self):
        return np.array([self._pos, self._vel, self._angle])

    def get_available_moves(self):
        return ('l','r', 'o')

    def __str__(self):
        x, v, a, z = self._pos, self._vel, self._angle, self._ang_vel
        result = f"""The cart is at position {x} travelling at speed {y}, the pole is at an angle {a} and with angular velocity {z}."""
        if self._game_over:
            result += " The pole has fallen over!"

    def make_move(self, move):
        if move = 'l':
            d = -1
        elif move = 'r':
            d = +1
        elif move = 'o':
            d = 0
        else:
            raise ValueError("Invalid move. Valid moved are " + self.get_available_moves().__str__())
        pos = self._pos + self._vel * self._time_step
        vel = self._vel + d * self._time_step
        angle = self._angle + self._ang_vel * self._time_step
        ang_vel = self._ang_vel + self._time_step * (
            - d / self._m * np.cos(angle)
            +  np.sin(angle)
            - 2 * np.sin(angle)**3 / np.cos(angle) * (ang_vel)**2
        )

        self._pos, self._vel, self._angle, self._ang_vel = pos, vel, angle, ang_vel

        if abs(self._angle) > np.pi/2:
            self._game_over = True

        reward = 0 if self._game_over else self._time_step
        return reward

    def pretty_print(self, move):
        track = "===o=====o===\n"
        if move == 'r':
           arrow = "     -->     "
        elif move == 'l':
           arrow = "     <--     "
        elif move == 'o':
           arrow = "     ---     "

        poles = [
            "             \n"
            "       __    \n"
            "    __/__    \n",

            "             \n"
            "       _/    \n"
            "    __/__    \n",

            "        _    \n"
            "       /     \n"
            "    __/__    \n",

            "    \        \n"
            "     \       \n"
            "    __\__    \n",

            "    |        \n"
            "     \       \n"
            "    __\__    \n",

            "     \       \n"
            "     |       \n"
            "    __\__    \n",

            "     \       \n"
            "      \      \n"
            "    __|__    \n",

            "     |       \n"
            "     |       \n"
            "    __\__    \n",

            "     |       \n"
            "      \      \n"
            "    __|__    \n",

            "      \      \n"
            "      |      \n"
            "    __|__    \n",

            #"      |      \n"
            #"      |      \n"
            #"    __|__    \n",

            "      /      \n"
            "      |      \n"
            "    __|__    \n",

            "       |     \n"
            "      /      \n"
            "    __|__    \n",

            "       |     \n"
            "       |     \n"
            "    __/__    \n",

            "       /     \n"
            "      /      \n"
            "    __|__    \n",

            "       /     \n"
            "       |     \n"
            "    __/__    \n",

            "       |     \n"
            "       /     \n"
            "    __/__    \n",

            "       |     \n"
            "       /     \n"
            "    __/__    \n",

            "        /    \n"
            "       /     \n"
            "    __/__    \n",

            "        _    \n"
            "       /     \n"
            "    __/__    \n",

            "             \n"
            "       _/    \n"
            "    __/__    \n",

            "             \n"
            "       __    \n"
            "    __/__    \n"
        ]

        pole = poles[int(round(self._angle + np.pi / 2) * len(poles) / np.pi,0))]

