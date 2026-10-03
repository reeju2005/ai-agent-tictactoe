import csv
class GameLogger:

    def __init__(self):
        self.records = []

    def record_position(
        self,
        game_number,
        move_number,
        agent_name,
        player,
        board,
        heuristic_details,
        nodes_evaluated,
        nodes_pruned
    ):

        self.records.append({
            "game": game_number,
            "move": move_number,
            "agent": agent_name,
            "player": player,

            # Convert 2D board into a simple string
            "board": "".join(
                cell
                for row in board
                for cell in row
            ),

            "win": heuristic_details["win"],
            "loss": heuristic_details["loss"],
            "threat": heuristic_details["threat"],
            "center": heuristic_details["center"],
            "corner": heuristic_details["corner"],
            "potential": heuristic_details["potential"],
            "heuristic": heuristic_details["total"],

            "nodes_evaluated": nodes_evaluated,
            "nodes_pruned": nodes_pruned
        })

    def save(self, filename):

        if not self.records:
            return

        with open(
            filename,
            "w",
            newline=""
        ) as file:

            fieldnames = self.records[0].keys()

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(self.records)