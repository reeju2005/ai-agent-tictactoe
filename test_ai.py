from board import TicTacToe
from minimax import Minimax


game = TicTacToe()
ai = Minimax()


# X has a winning move at (0, 2)
game.make_move((0, 0), "X")
game.make_move((0, 1), "X")

# O
game.make_move((1, 0), "O")
game.make_move((1, 1), "O")


print("Current board:")
game.print_board()


move = ai.choose_move(game, "X", depth=3)


print("\nAI chooses:", move)
print("Nodes evaluated:", ai.nodes_evaluated)
print("Nodes pruned:", ai.nodes_pruned)