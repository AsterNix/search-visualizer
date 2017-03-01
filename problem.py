"""
The Model class represents the problem model used by the agent
to find a path from the start state to a goal state

Seraphina Nix
10 Febraury 2017
"""


class Problem():
    """
    Constructs a new Problem from a given Network

    net: the Network underlying the Problem
    """
    def __init__(self, net):
        # save the params
        self.net = net

    """
    Converts a NetworkNode to a state representation
    """
    def convertToState(self, node):
        state = (node.lat, node.long)
        return state

    """
    Creates the start state for the problem
    """
    def startState(self):
        return self.convertToState(self.net.startNode)

    """
    Finds the set of all possible actions from a state.

    state: the state to find actions for
    """
    def actions(self, state):
        actionList = []
        node = self.net.nodeMap[state]
        for neighbor in node.neighbors:
            actionList.append(self.convertToState(neighbor))

        return actionList

    """
    Determines the next state after taking an action in a state

    state: the state the action was taken in
    action: the action taken
    """
    def result(self, state, action):
        nextNode = self.net.nodeMap[action]
        return self.convertToState(nextNode)

    """
    Determines the cost of taking an action in a state

    state: the state the action was taken in
    action: the action taken
    """
    def cost(self, state, action):
        node = self.net.nodeMap[state]
        neighbor = self.net.nodeMap[action]
        return node.costs[neighbor]

    """
    Determines whether or not a state is a goal state

    state: the state to check whether it is a goal
    """
    def goal(self, state):
        node = self.net.nodeMap[state]
        return node in self.net.goalNodes

    """
    Returns the list of goal states in the environment
    """
    def goalStates(self):
        goals = []
        for node in self.net.goalNodes:
            goals.append(self.convertToState(node))
        return goals
