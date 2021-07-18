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
from game import Game

class CartPole(Game):

    """Cartpole"""

    def __init__(self, pos, vel, angle, m, time_step=None):
        """Initializes the cartpole game """
        Game.__init__(self)
        self._pos = pos # position of the centre of the cart
        self._vel = vel # the velocity of the cart
        self._angle = angle # angle of the pole relative to vertical in radian
        self._ang_vel = 0 # angular velocity of the pole relative in radian
        self._m = m # the mass of the pole
        self._game_over = False
        self._time_step = 1 if time_step is None else time_step

    def get_cur_state(self):
        return np.array([self._pos, self._vel, self._angle])

    def get_available_moves(self):
        return ('l','r', 'o')

    def __str__(self):
        x, v, a, z = round(self._pos, 2), round(self._vel, 2) , round(self._angle * 180 / np.pi), round(self._ang_vel * 180 / np.pi)
        result = f"""The cart is at position {x} travelling at speed {v}, the pole is at an angle {a} degrees and with angular velocity {z} degrees per second."""
        if self._game_over:
            result += "\nThe pole has fallen over!"
        return result

    def make_move(self, move):
        if move == 'l':
            d = -1
        elif move == 'r':
            d = +1
        elif move == 'o':
            d = 0
        else:
            raise ValueError("Invalid move. Valid moved are " + self.get_available_moves().__str__())
        pos = self._pos + self._vel * self._time_step
        vel = self._vel + d * self._time_step
        angle = self._angle + self._ang_vel * self._time_step
        ang_vel = self._ang_vel + self._time_step * (
            - d / self._m * np.cos(self._angle)
            +  np.sin(self._angle)
#            - 2 * np.sin(self._angle)**3 / np.cos(self._angle) * (self._ang_vel)**2
        )

        self._pos, self._vel, self._angle, self._ang_vel = pos, vel, angle, ang_vel

        if abs(self._angle) > np.pi/2:
            self._game_over = True

        reward = 0 if self._game_over else self._time_step
        return reward

    def pretty_print(self, move):
        top = "\n"
        track = "===o=====o===\n"
        if move == 'r':
           arrow = "     -->     "
        elif move == 'l':
           arrow = "     <--     "
        elif move == 'o':
           arrow = "     ---     "

        poles = [
            "             \n"
            "    __       \n"
            "    __\__    \n",

            "    _        \n"
            "     \       \n"
            "    __\__    \n",

            "    \        \n"
            "     \       \n"
            "    __\__    \n",

            "     \       \n"
            "      \      \n"
            "    __|__    \n",

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


            "       /     \n"
            "      /      \n"
            "    __|__    \n",

            "        /    \n"
            "       /     \n"
            "    __/__    \n",

            "        _    \n"
            "       /     \n"
            "    __/__    \n",

            "             \n"
            "       __    \n"
            "    __/__    \n"
        ]
        pole = poles[
            max(min(int(
                np.floor((self._angle / np.pi + 1 / 2) * (len(poles)))
            ),len(poles)), 0)
        ]

        return top + pole + track + arrow


if __name__ == "__main__":
    cart_position = 0
    cart_velocity = 0
    pole_angle = np.random.random()*0.1 - 0.05
    pole_mass = 1
    game = CartPole(
        cart_position,
        cart_velocity,
        pole_angle,
        pole_mass,
        time_step=0.1
    )
    move = 'o'
    total_reward = 0
    while not game._game_over:
        print(game)
        print(game.pretty_print(move))
        valid_moves = ", ".join(game.get_available_moves())
        next_move = input(f"Which move? ({valid_moves}): ")
        move = 'o' if next_move == '' else next_move

        total_reward += game.make_move(move)
    else:
        print(game)
        print(f"You scored {round(total_reward,1)} points!")
