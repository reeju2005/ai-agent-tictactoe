from minimax import Minimax
from heuristic import Heuristic


class Agent:

    def __init__(self, name, player, depth, heuristic_weights=None):
        self.name = name
        self.player = player
        self.depth = depth

        self.heuristic = Heuristic(heuristic_weights)
        self.minimax = Minimax(self.heuristic)

    def choose_move(self, game):
        return self.minimax.choose_move(game, self.player, self.depth)

    def get_statistics(self):
        return {
            "nodes_evaluated": self.minimax.nodes_evaluated,
            "nodes_pruned": self.minimax.nodes_pruned,
        }

    def evaluate_position(self, game):
        opponent = "O" if self.player == "X" else "X"
        return self.heuristic.evaluate_details(game.board, self.player, opponent)