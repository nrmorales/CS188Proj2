# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util, math

from game import Agent

class ReflexAgent(Agent):
    """
        A reflex agent chooses an action at each choice point by examining
        its alternatives via a state evaluation function.

        The code below is provided as a guide.  You are welcome to change
        it in any way you see fit, so long as you don't touch our method
        headers.
      """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.
    
        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.
    
        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
    
        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        def euclideanDistance (p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2)
        
        def manhattanDistance (p1, p2):
            return util.manhattanDistance(p1, p2)
    
        foodDist = 0
        ghostDist = 0
        scaredTimes = 0
        for food in newFood:
            foodDist += euclideanDistance(newPos, food)
        for ghost in newGhostStates:
            ghostDist += euclideanDistance(newPos, ghost.getPosition())
        for time in newScaredTimes:
            scaredTimes += time
    
        "*** YOUR CODE HERE ***"
        return 15 * (1 / len(newFood)) + 60 * scaredTimes + 300 * ghostDist + 10 * (1 / foodDist)

def scoreEvaluationFunction(currentGameState):
        """
          This default evaluation function just returns the score of the state.
          The score is the same one displayed in the Pacman GUI.
        
          This evaluation function is meant for use with adversarial search agents
          (not reflex agents).
        """
        return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
        """
          This class provides some common elements to all of your
          multi-agent searchers.  Any methods defined here will be available
          to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.
        
          You *do not* need to make any changes here, but you can if you want to
          add functionality to all your adversarial search agents.  Please do not
          remove anything, however.
        
          Note: this is an abstract class: one that should not be instantiated.  It's
          only partially specified, and designed to be extended.  Agent (game.py)
          is another abstract class.
        """
        
        def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
            self.index = 0 # Pacman is always agent index 0
            self.evaluationFunction = util.lookup(evalFn, globals())
            self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
        """
          Your minimax agent (question 2)
        """
        
        def getAction(self, gameState):
            """
              Returns the minimax action from the current gameState using self.depth
              and self.evaluationFunction.
            
              Here are some method calls that might be useful when implementing minimax.
            
              gameState.getLegalActions(agentIndex):
                Returns a list of legal actions for an agent
                agentIndex=0 means Pacman, ghosts are >= 1
            
              Directions.STOP:
                The stop direction, which is always legal
            
              gameState.generateSuccessor(agentIndex, action):
                Returns the successor game state after an agent takes an action
            
              gameState.getNumAgents():
                Returns the total number of agents in the game
            """
            
            return self.newMinimax(gameState, self.depth, Directions.STOP, True)[1]
    
     
        def newMinimax(self, state, depth, prevAction, isPacman):
            if depth <= 0:
                return (self.evaluationFunction(state), prevAction)
            score = float("-inf")
            best_action = None
            
            for action in state.getLegalActions(0 if isPacman else 1):
                guess = self.newMinimax(state.generateSuccessor(0 if isPacman else 1, action), depth - 1, action, ~isPacman)
                if isPacman:
                    if guess[0] > score:
                        score = guess[0]
                        best_action = action
                else:
                    if guess[0] < score:
                        score = guess[0]
                        best_action = action
            return (score, best_action)
    
        
    

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    
    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
        
          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).
    
      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """
    
    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.
        
          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

