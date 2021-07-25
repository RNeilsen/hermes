from game import Game


class GameRunner(object):

    """The entity which runs a game, e.g. a poker dealer.
    Responsible for allowing players to interact with the game, facilitating their moves"""

    def __init__(self, game, players):
        """

        :game: The game the players will play
        :players: A list of players of the game.

        """
        self._game = game
        self._players = {i: player for i, player in enumerate(players)}

    def player_move(self):
        """Allow the next player to make their turn.
        :returns: None

        """
        player_name = self._game.get_next_player()
        observation = self._game.observe_game(player_name)
        possible_moves = self._game.get_available_moves()

        player = self._players[next_player_name]
        score = self._game.get_scoreboard()[player_name]
        player.update_score(score)

        next_move = player.select_move(observation, possible_moves)
        self._game.make_move(move)


