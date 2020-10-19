# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions


def key(state, agent):
    """
    Given a pacman game state and the index of the current playing agent,
    returns a key that uniquely identifies a pacman game state.

    Arguments:
    ----------
    - `state`: the current state of the game.
    - `agent`: the index of the current playing agent.

    Return:
    --------
    - A hashable key that uniquely identifies a pacman game state.
    """

    return (
            agent,
            state.getPacmanPosition(),
            state.getGhostPosition(1),
            state.getFood()
            )


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """

        bestAction = self.minimax(state)

        return bestAction

    def minimax(self, state):
        """
        Minimax value for Pacman in a given game state

        Argument:
        ---------
        - `state`: the current game state.

        Return:
        -------
        - Minimax value for Pacman in state `state`
        """

        maxUtility = float('-inf')
        bestAction = None

        # Remembers game states already visited. Like for A* graph-search.
        closed = set()

        nextStates = state.generatePacmanSuccessors()

        # Find the action that maximizes the utility of Pacman (max agent = 0)
        for nextState, action in nextStates:
            closed.add(key(nextState, 0))

            utility = self.min_value(nextState, closed)

            if utility > maxUtility:
                maxUtility = utility
                bestAction = action

        return bestAction

    def max_value(self, state, closed):
        """
        Minimax value in given state when Pacman is playing.

        Arguments:
        ----------
        - `state`: the current game state.
        - `closed`: set of already visited game states.

        Return:
        -------
        - Minimax value when Pacman is playing in state `state`.
        """

        if state.isWin():
            return -state.getScore()
        elif state.isLose():
            return state.getScore()

        v = float('-inf')

        for nextState, move in state.generatePacmanSuccessors():
            keyValue = key(nextState, 0)  # Pacman = agent 0

            # not visiting already visited states
            if keyValue not in closed:
                closed.add(keyValue)

                """
                Each recursive call should works on its own copy of closed.
                Python uses call by reference so we need to copy the set.
                """
                v = max(v, self.min_value(nextState, closed.copy()))

        return v

    def min_value(self, state, closed):
        """
        Minimax value in given state when ghost is playing.

        Arguments:
        ----------
        - `state`: the current game state.
        - `closed`: set of already visited game states.

        Return:
        -------
        - Minimax value when the ghost is playing in state `state`.
        """

        if state.isWin():
            return state.getScore()
        elif state.isLose():
            return -state.getScore()

        v = float('inf')

        for nextState, move in state.generateGhostSuccessors(1):
            keyValue = key(nextState, 1)  # Ghost = agent 1

            # not visiting already visited states
            if keyValue not in closed:
                closed.add(keyValue)

                """
                Each recursive call should works on its own copy of closed.
                Python uses call by reference so we need to copy the set.
                """
                v = min(v, self.max_value(nextState, closed.copy()))

        return v
