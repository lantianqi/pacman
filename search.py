# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

"""
# def depthFirstSearch(problem):
#     '''
#     Search the deepest nodes in the search tree first.

#     Your search algorithm needs to return a list of actions that reaches the
#     goal. Make sure to implement a graph search algorithm.

#     To get started, you might want to try some of these simple commands to
#     understand the search problem that is being passed in:

#     print("Start:", problem.getStartState())
#     print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
#     print("Start's successors:", problem.getSuccessors(problem.getStartState()))
#     '''
#     "*** YOUR CODE HERE ***"
#     # util.raiseNotDefined()
#     '''
#     generation time check, can find shorter solutions, but not OK for this project test cases
#     '''

#     stack = util.Stack()
#     # a node consists of a search state and the action_list leading to this state
#     start_state = problem.getStartState()
#     if problem.isGoalState(start_state):
#         return []
#     root_node = (start_state, [])
#     stack.push(root_node)
#     generated = set()
#     generated.add(start_state)

#     while not stack.isEmpty():
#         node = stack.pop()
#         state, action_list = node
#         if problem.isGoalState(state):
#             return action_list
#         else:
#             for succ in problem.getSuccessors(state):
#                 new_state, new_action, _cost = succ
#                 if problem.isGoalState(new_state):
#                     return action_list + [new_action]
#                 if new_state not in generated:
#                     new_node = (new_state, action_list + [new_action])
#                     stack.push(new_node)
#                     generated.add(new_state)


# def breadthFirstSearch(problem):
#     '''Search the shallowest nodes in the search tree first.'''
#     "*** YOUR CODE HERE ***"
#     '''
#     generation check
#     '''
#     queue = util.Queue()
#     start_state = problem.getStartState()
#     root_node = (start_state, [])
#     queue.push(root_node)
#     generated = set()
#     generated.add(start_state)

#     while not queue.isEmpty():
#         node = queue.pop()
#         state, action_list = node
#         if problem.isGoalState(state):
#             return action_list
#         else:
#             for succ in problem.getSuccessors(state):
#                 new_state, new_action, _cost = succ
#                 if new_state not in generated:
#                     new_node = (new_state, action_list + [new_action])
#                     queue.push(new_node)
#                     generated.add(new_state)
"""


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    """
    expansion time check
    """

    stack = util.Stack()
    # a node consists of a search state and the action_list leading to this state
    start_state = problem.getStartState()
    root_node = (start_state, [])
    stack.push(root_node)
    expanded = set()

    while not stack.isEmpty():
        node = stack.pop()
        state, action_list = node
        if state not in expanded:
            # expand
            expanded.add(state)
            if problem.isGoalState(state):
                return action_list
            for succ in problem.getSuccessors(state):
                new_state, new_action, _cost = succ
                new_node = (new_state, action_list + [new_action])
                stack.push(new_node)
            

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    """"
    expansion check
    """

    queue = util.Queue()
    start_state = problem.getStartState()
    root_node = (start_state, [])
    queue.push(root_node)
    expanded = set()

    while not queue.isEmpty():
        node = queue.pop()
        state, action_list = node
        if state not in expanded:
            # expand
            expanded.add(state)
            if problem.isGoalState(state):
                return action_list
            else:
                for succ in problem.getSuccessors(state):
                    new_state, new_action, _cost = succ
                    new_node = (new_state, action_list + [new_action])
                    queue.push(new_node)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    """
    expansion check
    """

    pQueue = util.PriorityQueue()
    start_state = problem.getStartState()
    # root_node has start_state, action_list [], and g_cost value 0
    root_node = (start_state, [], 0)
    # push root_node into pQueue, priority will be 0, which is the g_cost value
    pQueue.push(root_node, 0)
    expanded = set()

    while not pQueue.isEmpty():
        node = pQueue.pop()
        state, action_list, g_cost = node
        if state not in expanded:
            # expand
            expanded.add(state)
            if problem.isGoalState(state):
                return action_list
            else:
                for succ in problem.getSuccessors(state):
                    new_state, new_action, step_cost = succ
                    new_node = (new_state, action_list + [new_action], g_cost + step_cost)
                    pQueue.push(new_node, g_cost + step_cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # util.raiseNotDefined()

    pQueue = util.PriorityQueue()
    start_state = problem.getStartState()
    h = heuristic(start_state, problem)
    # root_node has start_state, action_list [], and g_cost 0
    root_node = (start_state, [], 0)
    q = 0 + h
    # push root_node into pQueue, priority will be q, the q_value
    pQueue.push(root_node, q)
    closeSet = set()
    best_g = dict()

    while not pQueue.isEmpty():
        node = pQueue.pop()
        state, action_list, g_cost = node
        if (not state in closeSet) or g_cost < best_g.get(state):
            closeSet.add(state)
            best_g[state] = g_cost
            if problem.isGoalState(state):
                return action_list
            else:
                for succ in problem.getSuccessors(state):
                    new_state, new_action, step_cost = succ
                    new_node = (new_state, action_list+[new_action], g_cost+step_cost)
                    pQueue.push(new_node, g_cost+step_cost+heuristic(new_state, problem))
                    # new_f = g_cost + step_cost + heuristic(new_state, problem)
                    # old_f = g_cost + heuristic(state, problem)
                    # if old_f > new_f:
                    #     print("############## inconsistent ##############")


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


if __name__ == "__main__":
    problem = SearchProblem()

    print(__name__)
