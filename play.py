from board import TicTacToe
from agents import Agent
from game_log import GameLogger


def play_game(game_number=1):

    game = TicTacToe()

    nexus_weights = {
        "threat": 133,
        "center": 130,
        "corner": 112,
        "potential": 5
    }

    titan_weights = {
        "threat": 5,
        "center": 5,
        "corner": 4,
        "potential": 1
    }


    nexus = Agent(
        name="NEXUS",
        player="X",
        depth=3,
        heuristic_weights=nexus_weights
    )

    titan = Agent(
        name="TITAN",
        player="O",
        depth=4,
        heuristic_weights=titan_weights
    )


    agents = {
        "X": nexus,
        "O": titan
    }

    logger = GameLogger()

    current_player = "X"
    move_number = 0

    print("       AI AGENT BATTLE")

    print("\nNEXUS = X")
    print("TITAN = O")

    game.print_board()

    while not game.is_terminal():

        agent = agents[current_player]

        print("\n")
        print(f"Move {move_number + 1}: {agent.name}")

        # AI chooses move
        move = agent.choose_move(game)

        # Make actual move
        game.make_move(
            move,
            current_player
        )

        move_number += 1

        print(f"{agent.name} chooses: {move}")

        game.print_board()

        # Evaluate ACTUAL resulting position
        details = agent.evaluate_position(game)

        stats = agent.get_statistics()

        print("\nHeuristic:")
        print(f"Threat:    {details['threat']}")
        print(f"Center:    {details['center']}")
        print(f"Corner:    {details['corner']}")
        print(f"Potential: {details['potential']}")
        print(f"Total:     {details['total']}")

        print("\nSearch:")
        print(
            f"Nodes evaluated: "
            f"{stats['nodes_evaluated']}"
        )

        print(
            f"Nodes pruned: "
            f"{stats['nodes_pruned']}"
        )

        # Record the actual position
        logger.record_position(
            game_number=game_number,
            move_number=move_number,
            agent_name=agent.name,
            player=current_player,
            board=game.board,
            heuristic_details=details,
            nodes_evaluated=stats["nodes_evaluated"],
            nodes_pruned=stats["nodes_pruned"]
        )

        # Switch player
        current_player = (
            "O"
            if current_player == "X"
            else "X"
        )

    winner = game.check_winner()

    print("game over!")

    if winner == "X":
        print("Winner: NEXUS")

    elif winner == "O":
        print("Winner: TITAN")

    else:
        print("Result: DRAW")

    print(f"Total moves: {move_number}")

    # Save position data
    logger.save("positions.csv")

    print("\nPosition data saved to positions.csv")


if __name__ == "__main__":
    play_game()