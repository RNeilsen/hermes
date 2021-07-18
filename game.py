"""Defines a Game class interface and methods. 
These methods should be implemented in a subclass for each specific game."""

class Game:
    def __init__(self):
        pass

    def get_cur_state(self):
        """Returns the current gamestate in computer-useable form
        Format: A 2-tuple, first part a list of player scores, second part the
        internal gamestate in some format"""
        pass

    def __str__(self):
        """Returns a pretty human-readable version of the current gamestate."""
        pass
    
    def get_available_moves(self):
        """Returns a list of the available moves from the current gamestate"""
        pass

    def make_move(self, move):
        """Makes a move in the current gamestate. Returns the new gamestate"""
        return self.get_cur_state()
