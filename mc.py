"""Defines a Game class interface and methods. 
These methods should be implemented in a subclass for each specific game."""

from game import Game

class Mornington(Game):
    def __init__(self):
        self.current_street = None
        self.winner = False

    def get_cur_state(self):
        """Returns the current gamestate in computer-useable form
        Format: A 2-tuple, first part a list of player scores, second part the
        internal gamestate in some format"""
        return(([(1 if self.winner else 0)], (self.current_street, self.winner)))

    def __str__(self):
        """Returns a human-readable version of the current gamestate"""
        return f'Current street: {self.current_street}' + (', you win!' if self.winner else '')
    
    def get_available_moves(self):
        """Returns a list of the available moves from the current gamestate."""
        if self.winner:
            return []
        else:
            return ['Oxford Street', 'Abbey Road', 'Brick Lane', 'Mornington Crescent']

    def make_move(self, move):
        """Makes a move in the current gamestate. Returns the new gamestate"""
        if move not in self.get_available_moves():
            raise Exception("Invalid move requested")
        
        self.current_street = move
        if move == 'Mornington Crescent':
            self.winner = True

        return self.get_cur_state()
