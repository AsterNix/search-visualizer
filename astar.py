"""
The AStar class represents an object capable of using A* Search to find a
path to goal state from a start state in a given Problem

Seraphina Gibson
23 February 2017
This file was completed ~3 hours into the assignment.
"""

import time
import heapq
import math

class AStar():
    """
    Creates a new AStar object

    model: a Problem model of the environment
    """
    def __init__(self, model):
        # save the params
        self.model = model
        self.nodecount = 0
        self.next_id = 1
        
    def output_ans(self, end_node, start_time, end_time, path_dict, max_frontier_size, path_found):
            print("A*:")
            if path_found:
                path = [end_node]
                current = end_node
                path_cost = path_dict[current][1]
                path_length = 1
                while current != self.model.startState(): # and loop_count < 15:
                    prev = current
                    current = path_dict[current][0]
                    path.insert(0, current)
                    entry = path_dict[current]
                    path_cost += entry[1]
                    path_length += 1
#                print("Path:")
                #for node in path:
                #    print("Traveled to:", node[0], ",", node[1])
                print("The path was:", path_length, "nodes long, with a cost of:", path_cost)
            else:
                print("No Path Found")
            print(max_frontier_size, "was the largest the frontier became")
            print(self.nodecount, "nodes were expanded")
            search_time = end_time - start_time
            print(search_time, "seconds of computation were used\n")
 
    '''
    Calculates the euclidean distance between two states
    '''
    def dist(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
    '''
    Calculates a heuristic function based on the euclidian distance between
    the node and the closest goal
    '''               
    def h(self, state):
        cost_list = []
        for goal in self.model.goalStates():
            cost_list.append(self.dist(state, goal))
        return min(cost_list)
            
    """
    Searches for a path from the start state to a goal state using the
    Problem model given to the constructor
    """
    def search(self):
        start_time = time.process_time()
        #this is the priority queue, prepopulated with the start node
        #the first number is f(state): the total cost up to this point
        #plus the heuristic value of this point
        #the second number is the cost up to this point, and the third number is
        #the number of nodes we have explored before getting here
        pq = [(self.h(self.model.startState()), 0, 0, self.model.startState())]
        #the future explored set, currently empty
        #this has to be a dict so there is constant time lookup of whether a node is explored
        #else on large networks where the explored set is very long, each node we check whether
        #it has been explored is O(N) which is unacceptable
        explored = {}
        
        #create a dict that will store the parent of each node as it is visited
        parents = {}
        parents[self.model.startState()] = self.model.startState(), 0

        path_found = False
        max_frontier_size = 1
        while(len(pq) > 0 and not path_found):
            #pop a node from the pq
            heuristic_cost, cost_to_now, priority, current = heapq.heappop(pq)
            #print("Current:",current)
            
            if self.model.goal(current):
                end_time = time.process_time()
                path_found = True
                self.output_ans(current, start_time, end_time, parents, max_frontier_size, path_found)
            
            if(current in explored):
                #print("skipping explored node")
                continue
            self.nodecount += 1            
#            if self.nodecount % 500 == 0:
#                print("Expanded:", self.nodecount)
#                print("Len explored:", len(explored))
                #break
            explored[current] = 1
            #expand the node
            actions =  self.model.actions(current)
            for action in actions:
                neighbor = self.model.result(current, action)
                #store away the parent of a possible neighbor, plus the cost to get there

                if neighbor not in explored:
#                    print("Neighbor:", neighbor, "Explored:", explored)
                    #else add them to the queue if they are not seen yet
                    path_cost = cost_to_now + self.model.cost(current, action)
                    heuristic_cost = path_cost + self.h(neighbor)
                    heapq.heappush(pq, (heuristic_cost, path_cost, self.next_id, neighbor) )
                    self.next_id += 1
                    if neighbor not in parents or parents[neighbor][2] > path_cost:
                        parents[neighbor] = current, self.model.cost(current, action), path_cost
            max_frontier_size = max(max_frontier_size, len(pq))
        if not path_found:
            end_time = time.process_time()
            self.output_ans(self.model.startState(), start_time, end_time, parents, max_frontier_size, path_found)
                
