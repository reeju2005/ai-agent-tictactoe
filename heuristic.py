class Heuristic:

    def __init__(self, weights=None):
        # Default heuristic weights
        self.weights = weights or {
            "threat": 10,
            "center": 3,
            "corner": 2,
            "potential": 1,
        }

    def evaluate(self, board, ai_player, opponent):
        details = self.evaluate_details(board, ai_player, opponent)
        return details["total"]

    def evaluate_details(self, board, ai_player, opponent):
        winner = self.check_winner(board)

        # Terminal states
        if winner == ai_player:
            return {
                "win": 100,
                "loss": 0,
                "threat": 0,
                "center": 0,
                "corner": 0,
                "potential": 0,
                "total": 100,
            }

        if winner == opponent:
            return {
                "win": 0,
                "loss": -100,
                "threat": 0,
                "center": 0,
                "corner": 0,
                "potential": 0,
                "total": -100,
            }

        # Raw feature counts
        threat = 0
        center = 0
        corner = 0
        potential = 0

        # Center control
        if board[1][1] == ai_player:
            center += 1
        elif board[1][1] == opponent:
            center -= 1

        # Corner control
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for row, col in corners:
            if board[row][col] == ai_player:
                corner += 1
            elif board[row][col] == opponent:
                corner -= 1

        # Winning lines
        lines = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        for line in lines:
            values = [board[row][col] for row, col in line]
            ai_count = values.count(ai_player)
            opponent_count = values.count(opponent)
            empty_count = values.count(" ")

            # AI threat (two in a row with open third cell)
            if ai_count == 2 and empty_count == 1:
                threat += 1

            # Opponent threat (two in a row with open third cell)
            if opponent_count == 2 and empty_count == 1:
                threat -= 1

            # Potential winning line (unblocked lines)
            if ai_count > 0 and opponent_count == 0:
                potential += 1
            elif opponent_count > 0 and ai_count == 0:
                potential -= 1

        # Apply strategy weights
        threat_score = threat * self.weights["threat"]
        center_score = center * self.weights["center"]
        corner_score = corner * self.weights["corner"]
        potential_score = potential * self.weights["potential"]

        total = threat_score + center_score + corner_score + potential_score

        return {
            "win": 0,
            "loss": 0,
            "threat": threat_score,
            "center": center_score,
            "corner": corner_score,
            "potential": potential_score,
            "total": total,
        }

    def check_winner(self, board):
        # Check rows
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return board[i][0]

        # Check columns
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != " ":
                return board[0][j]

        # Check main diagonal
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]

        # Check anti-diagonal
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]

        return None