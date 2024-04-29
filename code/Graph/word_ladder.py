#!/usr/bin/env python3

"""
word_ladder.py
Project description
"""
__author__ = "Max Ismagilov"
__version__ = "YYYY-MM-DD"

from atds import *

def letter_difference(w1, w2):
    ct = 0
    if w1 == w2 or len(w1) != len(w2):
        return ct
    for i in range(len(w1)):
        ct += 0 if w1[i] == w2[i] else 1
    return ct
        

def build_graph(wordlist):
    g = Graph()
    for word in wordlist:
        g.add_vertex(word)
    
    for word in wordlist:
        for otherword in wordlist:
            if letter_difference(word, otherword) == 1:
                g.add_edge(word, otherword)
    return g

def get_file(file):
    words = []
    infile = open(file)
    for line in infile:
        words.append(line.rstrip())
    return words
        
def bfs(graph, start):
    """Performs a BFS on `graph` beginning at `start` vertex, creating
    a series of predecessor links between the vertices.
    """
    start.set_distance(0)
    start.set_pred(None)
    queue = []
    queue.append(start)
    while len(queue) > 0:
        current_vertex = queue.pop(0)
        for n in current_vertex.get_connections():
            neighbor = graph.get_vertex(n)
            if neighbor.get_color() == 'white':
                neighbor.set_color('gray')
                neighbor.set_distance(current_vertex.get_distance() + 1)
                neighbor.set_pred(current_vertex)
                queue.append(neighbor)
        current_vertex.set_color('black')
        
def search_connection(graph: Graph, word1, word2):
    bfs(graph, graph.get_vertex(word1))
    current =  graph.get_vertex(word2)
    order = []
    while current.get_pred() != None:
        order.insert(0, current.get_id())
        current = current.get_pred()
    order.insert(0, current.get_id())
    return order

def main():
    g = build_graph(get_file("four_letter_words.txt"))
    o = search_connection(g, "SHIT", "FUCK")
    for i in o:
        print(i)
    
if __name__ == "__main__":
    main()
