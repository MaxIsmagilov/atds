#!/usr/bin/env python3

"""
graph_tester.py
Project description
"""
__author__ = "Max Ismagilov"
__version__ = "YYYY-MM-DD"

from atds import *

def main():
    g = Graph()
    for i in range(6):
        g.add_vertex(i)  # Create vertexes and add to the graph
    # Add a series of edges between the vertices
    g.add_edge(0,1,5)
    g.add_edge(0,5,2)
    g.add_edge(1,2,4)
    g.add_edge(2,3,9)
    g.add_edge(3,4,7)
    g.add_edge(3,5,3)
    g.add_edge(4,0,1)
    g.add_edge(5,4,8)
    g.add_edge(5,2,1)
    # Display all the vertices (possible because `iter` is defined)
    for vertex in g:
        print(vertex)
    for vertex1 in g:
        for vertex2 in vertex1.get_connections():
            print("( %s , %s )" % (vertex1, vertex2))

if __name__ == "__main__":
     main()
