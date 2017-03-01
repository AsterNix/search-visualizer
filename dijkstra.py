"""
The Dijkstra class represents an object capable of using Dijkstra's Method to find a
path to goal state from a start state in a given Problem

Seraphina Nix
23 February 2017

"""

import time
import heapq
import turtle
import draw as dr 

draw = False

class Dijkstra():
	"""
	Creates a new Dijkstra object

	model: a Problem model of the environment
	"""
	def __init__(self, model):
		# save the params
		self.model = model
		self.nodecount = 0
		self.next_id = 1    
	def outputAns(self, end_node, start_time, end_time, path_dict, max_frontier_size, path_found, d):
			print("Dijkstra:")
			if path_found:
				path = [end_node]
				current = end_node
				path_cost = path_dict[current][1]
				path_length = 1
				
				while current != self.model.startState(): # and loop_count < 15:
					current = path_dict[current][0]                
					path.insert(0, current)
					entry = path_dict[current]
					path_cost += entry[1]
					path_length += 1
				if draw:
					d.drawPath(path)
				#print("Path:")
				#for node in path:
				#    print("Traveled to:", node[0], ",", node[1])
				print("The path was:", path_length, "nodes long, with a cost of:", path_cost)
			else:
				print("No Path Found")
			print(max_frontier_size, "was the largest the frontier became")                
			print(self.nodecount, "nodes were expanded")
			search_time = end_time - start_time
			print(search_time, "seconds of computation were used\n")
			
				
			
	"""
	Searches for a path from the start state to a goal state using the
	Problem model given to the constructor
	"""
	def search(self):
		start_time = time.process_time()
		#this is the priority queue, prepopulated with the start node
		#the first number is the cost up to this point, the second number is
		#the number of nodes we have explored before getting here
		pq = [(0, 0, self.model.startState())]
		#the future explored set, currently empty
		#this has to be a dict so there is constant time lookup of whether a node is explored
		#else on large networks where the explored set is very long, each node we check whether
		#it has been explored is O(N) which is unacceptable
		explored = {}
		
		#create a dict that will store the parent of each node as it is visited
		#the tuple is formatted as follows:
		#parent, cost to traverse parent to child, path cost to this point
		parents = {}
		parents[self.model.startState()] = self.model.startState(), 0, 0
		
		if draw:
			d = dr.Draw(self.model.startState())
			d.drawGoals(self.model.goalStates())
		else:
			d = None
			
		path_found = False
		max_frontier_size = 1
		while(len(pq) > 0 and not path_found):
			#pop a node from the pq
			cost_to_now, priority, current = heapq.heappop(pq)
			
			if draw:
				d.visitPoint(current)
				
			#check if the neighbor is a  goal
			if self.model.goal(current):
				end_time = time.process_time()
				path_found = True
				self.outputAns(current, start_time, end_time, parents, max_frontier_size, path_found, d)
				break
				
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

					if draw:
						d.explorePoint(neighbor)

					#add them to the queue if they are not seen yet                    
					path_cost = cost_to_now + self.model.cost(current, action)
					heapq.heappush(pq, (path_cost, self.next_id, neighbor) )
					self.next_id += 1
					if neighbor not in parents or parents[neighbor][2] > path_cost:
						parents[neighbor] = current, self.model.cost(current, action), path_cost

			heapq.heapify(pq)
			#print("Current was:", current, "heap is:", pq)
			max_frontier_size = max(max_frontier_size, len(pq))
			
		if not path_found:
			end_time = time.process_time()
			self.outputAns(self.model.startState(), start_time, end_time, parents, max_frontier_size, path_found, d)
			
		if draw:
			input()    
			d.reset()