import random
class Minimax:

    def __init__(self, heuristic):
        self.heuristic = heuristic
        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    def reset_stats(self):
        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    def minimax(self, game, depth, maximizing, ai_player, opponent, alpha, beta):
        # Check terminal state
        winner = game.check_winner()

        if winner == ai_player:
            self.nodes_evaluated += 1
            return 100

        if winner == opponent:
            self.nodes_evaluated += 1
            return -100

        if game.is_board_full():
            self.nodes_evaluated += 1
            return 0

        # Depth limit reached
        if depth == 0:
            self.nodes_evaluated += 1
            return self.heuristic.evaluate(game.board, ai_player, opponent)

        # MAX player's turn
        if maximizing:
            best_score = float("-inf")
            for move in game.get_valid_moves():
                # Make temporary move
                game.make_move(move, ai_player)
                score = self.minimax(game, depth - 1, False, ai_player, opponent, alpha, beta)

                # Undo temporary move
                row, col = move
                game.board[row][col] = " "

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                # Alpha-Beta pruning
                if beta <= alpha:
                    self.nodes_pruned += 1
                    break

            return best_score

        # MIN player's turn
        else:
            best_score = float("inf")
            for move in game.get_valid_moves():
                # Make temporary move
                game.make_move(move, opponent)
                score = self.minimax(game, depth - 1, True, ai_player, opponent, alpha, beta)

                # Undo temporary move
                row, col = move
                game.board[row][col] = " "

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                # Alpha-Beta pruning
                if beta <= alpha:
                    self.nodes_pruned += 1
                    break

            return best_score

    # Choose best move
    def choose_move(self, game, player, depth):

        self.reset_stats()

        opponent = "O" if player == "X" else "X"

        best_score = float("-inf")
        best_moves = []

        alpha = float("-inf")
        beta = float("inf")

        for move in game.get_valid_moves():

            # Make temporary move
            game.make_move(move, player)

            score = self.minimax(game, depth - 1, False, player, opponent, alpha, beta)

            # Undo move
            row, col = move
            game.board[row][col] = " "

            if score > best_score:

                best_score = score
                best_moves = [move]

            elif score == best_score:

                best_moves.append(move)

            alpha = max(alpha, best_score)

        # Randomly select among equally good moves
        return random.choice(best_moves)