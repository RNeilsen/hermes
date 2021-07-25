class HumanPlayer(object):

    """A class facilitating a human playing the game"""

    def __init__(self):
        pass

    def select_move(self, observation, available_moves):
        """TODO: Docstring for select_move.

        :observation: An observation of the game.
        :available_moves: Moves which can be made in the game
        :returns: move to be made (selected by a human)

        """
        print(observation)
        valid_move_selected = False
        while not valid_move_selected:
            move = input(f"Which move? ({', '.join(available_moves)}): ")
            valid_move_selected = (move in available_moves)
            if not valid_move_selected:
                print("Invalid move! Please select again")
        return move

    def update_score(self, score):
        """Print the score.

        :score: the score in the game
        :returns: None. Prints the score

        """
        print(f"Your score is {score}")
