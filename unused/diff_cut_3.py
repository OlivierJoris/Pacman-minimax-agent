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
        self.maxDepth = 5
        self.init = True
        self.initNumFood = 0

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

        if self.init:
            self.initNumFood = state.getNumFood()
            init = False

        bestAction = self.hminimax(state, 0)

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

        if state.isLose() or state.isWin() or depth == self.maxDepth:
            return True

        return False

    def eval(self, state):
        """
        Given an agent game state, returns a numerical value that
        estimates this state.
        
        Arguments:
        ----------
        - `state`: the current game state.

        Return:
        -------
        - A numerical value that estimates the actual state.
        """

        pacmanPosition = state.getPacmanPosition()
        ghostPosition = state.getGhostPosition(1)

        ghostDistance = abs(pacmanPosition[0] - ghostPosition[0])\
                        + abs(pacmanPosition[1] - ghostPosition[1])

        #return 10*(self.initNumFood - state.getNumFood()) + 5*ghostDistance
        return - 10*state.getNumFood() + ghostDistance
 
    def hminimax(self, state, depth):
        """
        Minimax value for Pacman in a given game state

        Argument:
        ---------
        - `state`: the current game state.
        - `depth`: the current explored depth of the tree.

        Return:
        -------
        - Minimax value for Pacman in state `state`
        """

        maxEvalValue = float('-inf')

        # Remembers game states already visited. Like for A* graph-search.
        closed = set()
        nextStates = state.generatePacmanSuccessors()

        # Find the action that maximizes the utility of Pacman (max agent = 0)
        for nextState, action in nextStates:
            closed.add(key(nextState, 0))

            evalValue = self.min_value(nextState, closed, depth)

            if evalValue > maxEvalValue:
                maxEvalValue = evalValue
                bestAction = action
        
        return bestAction

    def max_value(self, state, closed, depth):
        """
        Minimax value in given state when Pacman is playing.

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
                newDepth = depth + 1

                """
                Each recursive call should works on its own copy of closed.
                Python uses call by reference so we need to copy the set.
                """
                v = max(v, self.min_value(nextState, closed.copy(), newDepth))

        return v

    def min_value(self, state, closed, depth):
        """
        Minimax value in given state when ghost is playing.

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
                newDepth = depth + 1

                """
                Each recursive call should works on its own copy of closed.
                Python uses call by reference so we need to copy the set.
                """
                v = min(v, self.max_value(nextState, closed.copy(), newDepth))

        return v
