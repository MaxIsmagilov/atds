#!/usr/bin/env python3

"""
adts.py
A collection of ADT classes
"""
__author__ = "Max Ismagilov"
__version__ = "2024-02-13"

import operator

class Stack:
    """This class creates a stack (wrapped around list)
    """
    
    def __init__(self) -> None:
        """constructor, takes no arguments
        """
        self.arr = []
        
    def push(self, value):
        """pushes to the stack
        """
        self.arr.append(value)
        
    def pop(self):
        """pops and returns the last value
        """
        try:
            return self.arr.pop(len(self.arr)-1)
        except:
            return None
    
    def peek(self):
        """peeks and returns the last value
        """
        try:
            return self.arr[len(self.arr)-1]
        except:
            return None
        
    def size(self):
        """returns the size of the stack
        """
        return len(self.arr)
    
    def is_empty(self):
        """returns whether this is empty
        """      
        return (self.size() == 0)
    
    def __repr__(self):
        return ("Stack has: [" + (self.arr.__repr__()) + "]")

class Queue:
    def __init__(self):
        self.arr = []
        
    def size(self):
        return len(self.arr)
        
    def enqueue(self, item):
        self.arr.append(item)
    
    def dequeue(self):
        return self.arr.pop(0)
        
    def is_empty(self):
        return len(self.arr) == 0
    
    def peek(self):
        return self.arr[0] 
    
    def __repr__(self):
        return ("Queue has: [*front*" + (self.arr.__repr__()) + "*end*]")
        
class Deque:
    def __init__(self) -> None:
        self.arr = []
        
    def add_front(self, item):
        self.arr.insert(0, item)
        
    def add_rear(self, item):
        self.arr.append(item)
        
    def remove_front(self):
        return self.arr.pop(0)
        
    def remove_rear(self):
        return self.arr.pop()
        
    def size(self):
        return len(self.arr)
    
    def is_empty(self):
        return len(self.arr) == 0

class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
        
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, value):
        self.data = value
        
    def set_next(self, value):
        self.next = value
        
    def __repr__(self) -> str:
        return f"Node(data: {self.data}, next:{self.next})"
        
class UnorderedList:
    def __init__(self) -> None:
        self.head = None
    
    def add(self, item):
        if (self.head == None):
            self.head = Node(item, None)
        else:
            head_val = self.head
            self.head = Node(item, head_val)
            
    def remove(self, item):
        while (self.search(item)):
            self.remove_first(item)
            
    def remove_first(self, item):
        """
        removes JUST the first instance of an item

        """
        n = self.head
        if (self.head == None):
            return
        if (self.head.get_data() == item):
            self.head = self.head.get_next()
            return
        while (n.get_next() != None and n.get_next().get_data() != item):
            n = n.get_next()
        if (n.get_next() != None):
            n = n.set_next(n.get_next().get_next())
            return
        return
    
    
    def is_empty(self):
        return self.head == None
    
    def length(self):
        count = 0
        n = self.head
        while (n != None):
            count += 1
            n = n.get_next()
        return count
    
    def append(self, item):
        if self.head == None:
            self.add(item)
            return
        n = self.head
        while (n.get_next() != None):
            n = n.get_next()
        n.set_next(Node(item, None))
        
    def index(self, item):
        count = -1
        n = self.head
        while (n != None):
            count += 1
            if (n.get_data() == item):
                return count
            n = n.get_next()
        return -1
        
    def search(self, item):
        return self.index(item) != -1
    
    def insert(self, pos, item):
        n = self.head
        for i in range(0, pos):
            n = n.get_next()
        next = Node(n.get_data(), n.get_next())
        n.set_data(item)
        n.set_next(next)
        
    def pop(self):
        if self.head == None:
            return None
        if self.head.get_next() == None:
            val = self.head.get_data()
        n = self.head
        while (n.get_next().get_next() != None):
            n = n.get_next()
        
        val = n.get_next()
        n.set_next(None)
        return val 
    
    def pop(self, pos=-1):
        if pos == -1:
            pos = self.length()-1
        if pos == 0:
            self.head = self.head.get_next()
            return
        n = self.head
        for i in range(0, pos-1):
            n = n.get_next()
        val = n.get_next().get_data()
        n.set_next(n.get_next().get_next())
        return val
        
    def __repr__(self): # literally just Mr. White's method
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result
        
class UnorderedListStack:
    def __init__(self) -> None:
        self.list = UnorderedList()
    
    def push(self, item):
        self.list.add(item)
    
    def pop(self):
        return self.list.pop(0)
    
    def peek(self):
        i = self.list.pop(0)
        self.list.add(i)
        return i;
    
    def size(self):
        return self.list.length()
    
    def is_empty(self):
        return self.list.length() == 0
            
class HashTable:    
    def __init__(self, size) -> None:
        self.width = size
        self.arr = [None for _ in range(size)]
        
    def __repr__(self) -> str:
        return self.arr.__repr__()
    
    def put(self, key, value):
        check = key % self.width
        while (self.arr[check] != None):
            if (self.arr[check][0] == key):
                break
            check += 1
        self.arr[check] = [key, value]
        
    def get(self, key):
        check = key % self.width
        while (self.arr[check] != None):
            if (self.arr[check][0] == key):
                return self.arr[check][1]
            check += 1
        return None
        
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right
        
    def __str__(self):
        return f"BinaryTree[key={self.value},left_child={self.left},right_child={self.right}]"
        
    def get_root_val(self):
        return self.value
    
    def set_root_val(self, value):
        self.value = value
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def insert_left(self, value):
        btleft = BinaryTree(value, left=self.left)
        self.left = btleft
        
    def insert_right(self, value):
        btright = BinaryTree(value, right=self.right)
        self.right = btright
        
class BinaryHeap:
    def __init__(self) -> None:
        self.array = []
        
    def __repr__(self) -> str:
        return 'BinaryHeap' + str([0] + self.array)
        
    def sift_down(self, pos):
        left_child = lambda a: (a * 2 + 1)
        root = pos
        while( left_child(root) < len(self.array)):
            child = left_child(root)
            if (child+1 < len(self.array)):
                if (self.array[child] > self.array[child+1]):
                    child += 1
            if (self.array[root] > self.array[child]):
                self.array[root], self.array[child] = self.array[child], self.array[root]
                root = child
            else: 
                return
            
    def sift_up(self, pos):
        get_parent = lambda a: (a-1)//2
        child = pos
        while (get_parent(child) >= 0):
            print("DEBUG: " + str(self.array) + "  " + str(self.array[child]))
            parent = get_parent(child)
            if (self.array[child] < self.array[parent]):
                print("DEBUG: SWITCHED")
                self.array[parent], self.array[child] = self.array[child], self.array[parent]
                child = parent
            else:
                return            
        
    def insert(self, value):
        self.array.append(value)
        self.sift_up(len(self.array) - 1)
            
    def find_min(self):
        return None if len(self.array) == 0 else self.array[0]
    
    def del_min(self):
        if len(self.array) == 0:
            return
        self.array[0], self.array[len(self.array)-1] = self.array[len(self.array)-1], self.array[0]
        val = self.array.pop()
        self.sift_down(0)
        return val
        
    def is_empty(self):
        return len(self.array) == 0
    
    def size(self):
        return len(self.array)
    
    def build_heap(self, value_list):
        self.array = value_list
        heap_start = len(value_list) // 2
        while (heap_start > 0):
            heap_start -= 1
            self.sift_down(heap_start)
 
class TreeNode(object):
    """This class, as written, uses the fact that the Python value
    None has a Boolean value of False when used in boolean expressions.
    """
    def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        
    def get_key(self):
        return self.key

    def set_left_child(self, newchld):
        self.left_child = newchld
        newchld.parent = self

    def set_right_child(self, newchld):
        self.right_child = newchld
        newchld.parent = self
    
    def get_left_child(self):
        """returns the left child
        """
        return self.left_child 

    def get_right_child(self):
        """returns the right child
        """
        return self.right_child

    def is_left_child(self):
        """Returns True if this node is the left child of a parent """
        return False if self.parent == None else self.parent.get_left_child().get_key() == self.key

    def is_right_child(self):
        """Returns False if this node is the left child of a parent """
        return False if self.parent == None else self.parent.get_right_child().get_key() == self.key

    def is_root(self):
        """Return true if this is the root node """
        return self.parent == None

    def is_leaf(self):
        """Return true if we're a leaf node """
        return (self.right_child == None and self.left_child == None)

    def has_any_children(self):
        """Return true if at least one child exists """
        return (self.right_child != None or self.left_child != None)

    def has_both_children(self):
        """Return true if both children exist"""
        return (self.right_child != None and self.left_child != None)

    def replace_node_data(self, key, value, lc, rc):
        """Replaces the node data for a specific node"""
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self
            
    def get_value(self):
        return self.val
    
    def set_value(self, newval):
        self.val = newval

    def __iter__(self):
        """Recursive function that allows us to iterate through the BST
        keys using a loop! What?!!
        """
        if self:
            if self.has_left_child():
                for elem in self.left:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right:
                    yield elem

    def __repr__(self):
        return "TreeNode[key=" + str(self.key) \
             + ",value=" + str(self.value) \
             + ",left_child=" + str(self.left_child) \
             + ",right_child=" + str(self.right_child) + "]"
             
class BinarySearchTree(object):

    def __init__(self):
        """Creates a tree with an empty root reference and a
        size of 0"""
        self.tree = None
        self.size = 0

    def length(self):
        """Returns the size of the tree (how many nodes)"""
        return self.size

    def __len__(self):
        """Also returns the size of the tree. Allows us to use the
        len() method in Python."""
        return self.size

    def __iter__(self):
        """Allows us to iterate through the binary tree. ?!"""
        return self.root.__iter__()

    def _find(self, key, current: TreeNode):
        """finds either the closest value or the actual value of the key in the tree
        """
        k = current.get_key()
        c = None
        if k == key:
            return current
        elif k < key:
            c = current.get_right_child()
        else:
            c = current.get_left_child()
        return self._find(key, c) if c != None else current
            

    def put(self, key, val):
        if self.size == 0:
            self.tree = TreeNode(key, val, None, None, None)
            self.size = 1
        node: TreeNode = self._find(key, self.tree)
        if node.get_key() == key:
            node.set_value(val)
        else:
            self.size += 1
            if node.get_key() > key:
                node.set_left_child(TreeNode(key, val, None, None, node))
            else:
                node.set_right_child(TreeNode(key, val, None, None, node))
            

    def get(self, key):
        if self.size == 0: 
            return None
        node = self._find(key, self.tree)
        if node.get_key() == key:
            return node
        return None

class Vertex:
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary
        "connected_to" where we'll store other vertices to which this vertex is connected.
        """
        self.id = key
        self.connected_to = dict()
        self.color = 'white'
        self.distance = 0
        self.predecessor = None
        self.discovery_time = 0     
        self.finish_time = 0        

    def add_neighbor(self, neighbor_vertex, weight=0):
        """Adds a reference to a neighboring Vertex object to the dictionary, 
        to which this vertex is connected by an edge. If a weight is not indicated, 
        default weight is 0.
        """
        self.connected_to.update({neighbor_vertex : weight})

        
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_distance(self, distance):
        self.distance = distance
    
    def get_distance(self):
        return self.distance
    
    def set_pred(self, predecessor):
        self.predecessor = predecessor
    
    def get_pred(self):
        return self.predecessor
    
    def set_discovery(self, discovery_time):
        self.discovery_time = discovery_time
    
    def get_discovery(self):
        return self.discovery_time
    
    def set_finish(self, finish_time):
        self.finish_time = finish_time
    
    def get_finish(self):
        return self.finish_time
    
    def __repr__(self):
        """Returns a representation of the vertex and its neighbors,
        suitable for printing. Check out the example of 'list
        comprehension' here!
        """
        return 'Vertex[id=' + str(self.id) \
                + ',color=' + self.color \
                + ',dist=' + str(self.distance) \
                + ',pred=' + str(self.predecessor) \
                + ',disc=' + str(self.discovery_time) \
                + ',fin=' + str(self.finish_time) \
              + '] connected_to: ' + str([x for x in self.connected_to]) 
              
    def get_connections(self):
        """Returns the keys of the vertices we're connected to
        """
        return [x for x in self.connected_to]

    def get_id(self):
        """Returns the id ("key") for this vertex
        """
        return self.id

    def get_weight(self, neighbor_vertex):
        """Returns the weight of an edge connecting this vertex with another.
        """
        return None if neighbor_vertex not in self.connected_to else self.connected_to[neighbor_vertex]

class Graph:
    """Describes the Graph class, which is primarily a dictionary  
    mapping vertex names to Vertex objects, along with a few methods 
    that can be used to manipulate them.
    """
    def __init__(self):
        """Initializes an empty dictionary of Vertex objects
        """
        self.vertices = dict()

    def add_vertex(self, key):
        """Creates a new "key-value" dictionary entry with the string "key"
        key as the dictionary key, and the Vertex object itself as the value. 
        Returns the new vertex as a result.
        """
        self.vertices.update({key : Vertex(key)})

    def get_vertex(self, key):
        """Looks for the key in the dictionary of Vertex objects, and 
        returns the Vertex if found. Otherwise, returns None.
        """
        return None if key not in self.vertices else self.vertices[key]

    def __contains__(self, key):
        """This 'dunder' expression is written so we can use Python's "in" 
        operation: If the parameter 'key' is in the dictionary of vertices,
        the value of "key in my_graph" will be True, otherwise False.
        """
        return key in self.vertices

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Adds an edge connecting two vertices (specified by key parameters)
        by modifying those vertex objects. Note that the weight can be 
        specified as well, but if one isn't specified, the value of weight 
        will be the default value of 0.
        """
        self.vertices[from_vertex].add_neighbor(to_vertex, weight)

    def get_vertices(self):
        """Returns a list of the Vertex keys"""
        return [x for x in self.vertices]

    def __iter__(self):
        """Another 'dunder' expression that allows us to iterate through
        the list of vertices.
        Example use:
        for vert in graph:  # Python understands this now!
            print(v)
        """
        return iter(self.vertices.values())