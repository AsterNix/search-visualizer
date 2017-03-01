"""
The IterDeep class represents an objet capable of using Iterative Deepening Search to find a
path to goal state from a start state in a given Problem

Seraphina Nix
22 February 2017
This file was first completed ~4 hours into the project.
"""

import time
import draw as dr 

draw = False

class IterDeep():
	"""
	Creates a new BFS object

	model: a Problem model of the environment
	"""
	def __init__(self, model):
		# save the params
		self.model = model
		self.nodecount = 0
		self.start_time = -1
		self.end_time = -1
	
	def outputAns(self, end_node, start_time, end_time, path_dict, max_frontier_size, path_found):
			print("Iterative Deepening:")
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
				
				if draw:
					d.drawPath(path)
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
		path_found = False
		depth = 1
		while not path_found:
			print("Depth:", depth)
			path_found = self.depthLimitedSearch(depth)
			depth += 1
			time.sleep(.5)
			
			
		print("Final Depth:", depth - 1)
		
	
	"""
	Performs DFS to a limited depth
	"""
	def depthLimitedSearch(self, depth_limit):

		#this is the queue, prepopulated with the start node
		q = [(0, self.model.startState())]

		#create a dict that will store the parent of each node as it is visited
		parents = {}
		parents[self.model.startState()] = self.model.startState(), 0, 0
		
		if draw:
			d = dr.Draw(self.model.startState())
			d.drawGoals(self.model.goalStates())
		else:
			d = None
			
		path_found = False
		max_frontier_size = 1
		while(len(q) > 0 and not path_found):
			#pop a node from the q
			depth, current = q.pop()
			if draw:
				d.visitPoint(current)
				
			#if it's too deep in the tree
			if(depth > depth_limit):
				continue
			self.nodecount += 1


			#expand the node
			actions =  self.model.actions(current)
			for action in actions:
				neighbor = self.model.result(current, action)
				#store away the parent of a possible neighbor, plus the cost to get there

				#check if the neighbor is a  goal
				if self.model.goal(neighbor):
					
					if draw:
						d.explorePoint(neighbor)
						
					parents[neighbor] = current, self.model.cost(current, action), depth 
					self.end_time = time.process_time()
					path_found = True
					self.outputAns(neighbor, self.start_time, self.end_time, parents, max_frontier_size, path_found)
					return path_found
				elif depth < depth_limit:
				
					if draw:
						d.explorePoint(neighbor)
						
					#else add them to the queue if they are not too deep
					q.append((depth+1, neighbor))
					if neighbor not in parents or parents[neighbor][2] > depth:
						parents[neighbor] = current, self.model.cost(current, action), depth
			max_frontier_size = max(max_frontier_size, len(q))
	
		return path_found 
				
