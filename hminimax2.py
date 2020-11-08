# Maxime Goffart (20180521) and Olivier Joris (20182113)

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
        self.maxDepth = 4
        self.playedStates = set()

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

        bestAction = self.hminimax(state, 0)
        self.playedStates.add(key(state.generateSuccessor(0, bestAction), 0))

        return bestAction

    def cutoff_test(self, state, depth):
        """
        Given the current game state and the current explored depth
        of the tree, check if the computations should stop now.

        Arguments:
        ----------
        - `state`: the current game state.
        - `depth`: the current explored depth of the tree.

        Return:
        -------
        - True if we have to stop the computations. Else, False.
        """

        if state.isLose() or state.isWin() or depth >= self.maxDepth:
            return True

        pacmanPosition = state.getPacmanPosition()

        ghostPosition = state.getGhostPosition(1)
        pacmanGhostDistance = abs(pacmanPosition[0] - ghostPosition[0])\
            + abs(pacmanPosition[1] - ghostPosition[1])

        foodMatrix = state.getFood()

        pacmanClosestFoodDistance = float('+inf')

        for i in range(foodMatrix.width):
            for j in range(foodMatrix.height):
                if foodMatrix[i][j]:
                    distancePacman = abs(pacmanPosition[0] - i)\
                                     + abs(pacmanPosition[1] - j)

                    if distancePacman < pacmanClosestFoodDistance:
                        pacmanClosestFoodDistance = distancePacman

        if pacmanGhostDistance >= pacmanClosestFoodDistance:
            return True

        return False

    def eval(self, state):
        """
        Given a game state, returns an estimate of the exepected utility.

        Arguments:
        ----------
        - `state`: a game state.

        Return:
        -------
        - A numerical value that estimates the expected utility.
        """

        pacmanPosition = state.getPacmanPosition()
        foodMatrix = state.getFood()
        ghostPosition = state.getGhostPosition(1)
        pacmanGhostDistance = abs(pacmanPosition[0] - ghostPosition[0])\
            + abs(pacmanPosition[1] - ghostPosition[1])

        if state.isLose() or state.isWin():
            pacmanClosestFoodDistance = 0  # no food left in the maze
            utility = state.getScore() - pacmanClosestFoodDistance\
                - 3*state.getNumFood()
            if pacmanGhostDistance == 0:
                return utility
            else:
                return utility - 1/pacmanGhostDistance

        pacmanClosestFoodDistance = float('+inf')

        for i in range(foodMatrix.width):
            for j in range(foodMatrix.height):
                if foodMatrix[i][j]:
                    distance = abs(pacmanPosition[0] - i)\
                               + abs(pacmanPosition[1] - j)
                    if distance < pacmanClosestFoodDistance:
                        pacmanClosestFoodDistance = distance

        return state.getScore() - pacmanClosestFoodDistance\
            - 3 * state.getNumFood() - 1 / pacmanGhostDistance

    def hminimax(self, state, depth):
        """
        H-Minimax value for Pacman in a given game state.

        Arguments:
        ----------
        - `state`: the current game state.
        - `depth`: the current explored depth of the tree.

        Return:
        -------
        - Minimax value for Pacman in state `state`.
        """

        maxEvalValue = float('-inf')

        # Remembers game states already visited. Like for A* graph-search.
        closed = set()
        nextStates = state.generatePacmanSuccessors()
        bestAction = None

        # Find the action that maximizes the utility of Pacman (max agent = 0)
        for nextState, action in nextStates:

            evalValue = self.min_value(nextState, closed, depth)

            keyValue = key(nextState, 0)

            # Avoid to repeat look for already played and visited states
            if keyValue not in self.playedStates\
                and keyValue not in closed\
                    and evalValue > maxEvalValue:

                maxEvalValue = evalValue
                bestAction = action
                closed.add(keyValue)

        return bestAction

    def max_value(self, state, closed, depth):
        """
        H-Minimax value in a given state when Pacman is playing.

        Arguments:
        ----------
        - `state`: the current game state.
        - `closed`: set of already visited game states.
        - `depth`: the current explored depth of the tree.

        Return:
        -------
        - Minimax value when Pacman is playing in state `state`.
        """

        if self.cutoff_test(state, depth):
            return self.eval(state)

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
                v = max(v, self.min_value(nextState, closed.copy(), depth + 1))

        return v

    def min_value(self, state, closed, depth):
        """
        H-Minimax value in given state when ghost is playing.

        Arguments:
        ----------
        - `state`: the current game state.
        - `closed`: set of already visited game states.
        - `depth`: the current explored depth of the tree.

        Return:
        -------
        - Minimax value when the ghost is playing in state `state`.
        """

        if self.cutoff_test(state, depth):
            return self.eval(state)

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
                v = min(v, self.max_value(nextState, closed.copy(), depth + 1))

        return v
