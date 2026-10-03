# AI Agent Battle – Tic-Tac-Toe

## Project Overview

AI Agent Battle is a Python-based Artificial Intelligence project that implements two autonomous AI agents, **NEXUS** and **TITAN**, competing against each other in Tic-Tac-Toe. The project demonstrates the application of adversarial search algorithms, heuristic evaluation, and Alpha-Beta pruning in a two-player, zero-sum game.

## AI Agents

The project contains two AI agents with different evaluation strategies.

**NEXUS** prioritizes immediate threats, center control, and potential winning lines.

**TITAN** uses a different balance of heuristic factors, being more tactical and flexible.


## Project Structure

The project is organized into separate Python modules:

* `game.py` – Implements the Tic-Tac-Toe game engine, including board initialization, valid moves, move execution, and winner detection.
* `heuristic.py` – Implements the heuristic evaluation function used to calculate the value of a board position.
* `minimax.py` – Implements Minimax with Alpha-Beta pruning and tracks evaluated nodes and pruning events.
* `agents.py` – Defines the AI Agent class and configures the agents.
* `game_logger.py` – Records individual game positions and evaluation statistics.
* `play_game.py` – Runs an individual game between NEXUS and TITAN.
* `experiment.py` – Executes multiple AI-vs-AI games and collects battle statistics.
* `positions.csv` – Stores position-level evaluation data.
* `battle_results.csv` – Stores the results and performance statistics of the battle experiment.

## How to Run

Run the following command to execute an individual game:

   `python play_game.py`

To execute the 200-game experiment, run:

   `python experiment.py`