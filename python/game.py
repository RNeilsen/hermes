"""Defines a Game class interface and methods. 
These methods should be implemented in a subclass for each specific game."""

class Game:
    def __init__(self):
        pass

    def get_cur_state(self):
        """Returns the current gamestate in computer-useable form"""
        pass

    def print_state(self, gamestate):
        """Print a pretty human-readable version of a given gamestate.
        Can be passed 'None' for gamestate to print the current gamestate"""
        pass
    
    def get_available_moves(self, gamestate):
        """Returns a list of the available moves from a given gamestate
        Can be passed 'None' for gamestate to print the current gamestate"""
        pass

    def make_move(self, move):
        """Makes a move in the current gamestate. Returns the new gamestate"""
        pass