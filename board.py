class TicTacToe:

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player1 = "O"
        self.player2 = "X"

    def print_board(self):
        for i in range(3):
            print(
                f"{self.board[i][0]} | "
                f"{self.board[i][1]} | "
                f"{self.board[i][2]}"
            )

            if i < 2:
                print("---------")

    # Return all empty cells
    def available_moves(self):
        moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    moves.append((i, j))

        return moves

    # Same function with the name used in the assignment
    def get_valid_moves(self):
        return self.available_moves()

    # Make a move
    def make_move(self, position, player):

        row, col = position

        if self.board[row][col] == " ":
            self.board[row][col] = player
            return True

        return False

    # Check whether the board is full
    def is_board_full(self):
        return all(" " not in row for row in self.board)

    # Check winner
    def check_winner(self):

        # Check rows
        for i in range(3):

            if (
                self.board[i][0]
                == self.board[i][1]
                == self.board[i][2]
                != " "
            ):
                return self.board[i][0]

        # Check columns
        for j in range(3):

            if (
                self.board[0][j]
                == self.board[1][j]
                == self.board[2][j]
                != " "
            ):
                return self.board[0][j]

        # Check main diagonal
        if (
            self.board[0][0]
            == self.board[1][1]
            == self.board[2][2]
            != " "
        ):
            return self.board[0][0]

        # Check other diagonal
        if (
            self.board[0][2]
            == self.board[1][1]
            == self.board[2][0]
            != " "
        ):
            return self.board[0][2]

        return None

    # Check whether game has ended
    def game_over(self):
        return (
            self.check_winner() is not None
            or self.is_board_full()
        )

    # Name used by Minimax
    def is_terminal(self):
        return self.game_over()


# Test
if __name__ == "__main__":

    game = TicTacToe()

    game.print_board()

    print("\nAvailable moves:")
    print(game.available_moves())

    print("\nMaking moves...")

    game.make_move((0, 0), "X")
    game.make_move((1, 1), "O")
    game.make_move((0, 1), "X")

    game.print_board()

    print("\nAvailable moves:")
    print(game.available_moves())

    print("\nWinner:", game.check_winner())
    print("Game over:", game.game_over())