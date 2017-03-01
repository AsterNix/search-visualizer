"""
Main represents the main execution flow of the program

Adam Eck
02/11/2017
"""

import astar
import beams
import bfs
import dijkstra
import iterativedeepening
import network
import problem
import sys


"""
Runs the program with both BFS and A*
"""
def main():
    # validate the params
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <NETWORK_FILE>")
        sys.exit(-1)

    # read in the network from file
    net = network.readFromFile(sys.argv[1])

    # create the problem model
    model = problem.Problem(net)

    # search using BFS
    bfsSearcher = bfs.BFS(model)
    bfsSearcher.search()

    # search using dijkstra
    dijkstraSearcher = dijkstra.Dijkstra(model)
    dijkstraSearcher.search()

    # search using A*
    astarSearcher = astar.AStar(model)
    astarSearcher.search()
    
    # search using beam search
    beamSearcher = beams.Beams(model)
    beamSearcher.search()
    
    # search using Iterative Deepening
    idSearcher = iterativedeepening.IterDeep(model)
    idSearcher.search()

if (__name__ == "__main__"):
    main()
