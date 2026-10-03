
import csv
import time

from board import TicTacToe
from agents import Agent


nexus_weights = {
    "threat": 25,
    "center": 6,
    "corner": 4,
    "potential": 5
}

titan_weights = {
    "threat": 8,
    "center": 1,
    "corner": 4,
    "potential": 2
}


def run_game(game_number, first_player):

    game = TicTacToe()

    nexus = Agent(
        name="NEXUS",
        player="X",
        depth=3,
        heuristic_weights=nexus_weights
    )

    titan = Agent(
        name="TITAN",
        player="O",
        depth=3,
        heuristic_weights=titan_weights
    )

    agents = {
        "X": nexus,
        "O": titan
    }

    current_player = first_player
    moves = 0

    nexus_nodes = 0
    titan_nodes = 0
    nexus_pruned = 0
    titan_pruned = 0

    start_time = time.perf_counter()

    while not game.is_terminal():

        agent = agents[current_player]

        move = agent.choose_move(game)
        game.make_move(move, current_player)

        moves += 1

        stats = agent.get_statistics()

        if agent.name == "NEXUS":
            nexus_nodes += stats["nodes_evaluated"]
            nexus_pruned += stats["nodes_pruned"]
        else:
            titan_nodes += stats["nodes_evaluated"]
            titan_pruned += stats["nodes_pruned"]

        current_player = "O" if current_player == "X" else "X"

    execution_time = time.perf_counter() - start_time

    winner_symbol = game.check_winner()

    if winner_symbol is None:
        winner = "Draw"
    else:
        winner = agents[winner_symbol].name

    first_agent = agents[first_player].name

    return {
        "Game": game_number,
        "First Player": first_agent,
        "Winner": winner,
        "Moves": moves,
        "NEXUS Nodes": nexus_nodes,
        "TITAN Nodes": titan_nodes,
        "NEXUS Pruned": nexus_pruned,
        "TITAN Pruned": titan_pruned,
        "Execution Time": round(execution_time, 6)
    }


def run_battle(number_of_games=10):

    results = []

    for game_number in range(1, number_of_games + 1):

        if game_number % 2 == 1:
            first_player = "X"
        else:
            first_player = "O"

        result = run_game(game_number, first_player)
        results.append(result)

        print(
            f"Game {game_number}: "
            f"First = {result['First Player']}, "
            f"Winner = {result['Winner']}, "
            f"Moves = {result['Moves']}"
        )

    with open("battle_results.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    nexus_wins = sum(
        1 for result in results
        if result["Winner"] == "NEXUS"
    )

    titan_wins = sum(
        1 for result in results
        if result["Winner"] == "TITAN"
    )

    draws = sum(
        1 for result in results
        if result["Winner"] == "Draw"
    )

    print("\n========== BATTLE SUMMARY ==========")
    print("NEXUS Wins:", nexus_wins)
    print("TITAN Wins:", titan_wins)
    print("Draws:", draws)
    print("Total Games:", number_of_games)
    print("\nResults saved to battle_results.csv")


if __name__ == "__main__":
    run_battle(200)