"""
vertex_tester.py
Project description
"""
__author__ = "Max Ismagilov"
__version__ = "YYYY-MM-DD"


from atds import Vertex

def main():
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v1.add_neighbor(v2)
    v1.add_neighbor(v3,7)
    print("Vertex v1 is ", v1)
    print("Vertex v1 is connected to ", v1.get_connections())
    print("The weight between v1 and v3 is ", v1.get_weight(v3))
    print("Vertex v2 is connected to ", v2.get_connections())#!/usr/bin/env python3

if __name__ == "__main__":
     main()



