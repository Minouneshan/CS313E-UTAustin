#  File: Graph.py

#  Description: This program performs a depth first search and breadth first search on a graph of cities.

#  Student Name: Mohamad Minoneshan

#  Partner Name: Mercedes Milke

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/18/2022

#  Date Last Modified: 11/18/2022

import sys

class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        num_vertices = len(self.Vertices)
        for i in range(num_vertices):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        num_vertices = len(self.Vertices)
        for i in range(num_vertices):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):

        # do nothing if the vertex is already in the graph
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):

        # find the respective indices of the labels
        row_index = self.get_index(fromVertexLabel)
        column_index = self.get_index(toVertexLabel)

        # handle case where labels are invalid
        if (row_index == -1 or column_index == -1):
            return -1

        # the labels are connected by an edge
        if (self.adjMat[row_index][column_index] != 0):
            return self.adjMat[row_index][column_index]

        # the labels are not connected
        else:
            return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors(self, vertexLabel):

        # find the index of the row to check
        row = self.get_index(vertexLabel)

        # create an empty neighbors list
        neighbors_list = []

        # traverse through the row and find which other labels to
        # which the given label is connected
        for col in range (len(self.adjMat[row])):
            if (self.adjMat[row][col] != 0):
                neighbors_list.append(col)

        # return the neighbors list
        return neighbors_list

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        num_vertices = len(self.Vertices)
        for i in range(num_vertices):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices(self):
        num_vertices = len(self.Vertices)
        vertex_list = []
        for i in range(num_vertices):
            vertex_list.append(self.Vertices[i])
        return vertex_list

    # do a depth first search in a graph
    def dfs(self, v):

        # create the Stack
        the_stack = Stack()

        # mark the vertex v as visited and push it on the stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        the_stack.push(v)

        # visit all the other vertices according to depth
        while (not the_stack.is_empty()):

            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(the_stack.peek())

            # if there are no vertices left to visit, pop a vertex
            # from the stack and make it the current vertex
            if (u == -1):
                u = the_stack.pop()

            # mark the adjacent vertex as visited and make it the
            # current vertex
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                the_stack.push(u)

        # the stack is empty, reset the flags
        num_vertices = len(self.Vertices)
        for i in range(num_vertices):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):

        # create the Queue
        the_queue = Queue()

        # make the starting vertex the current vertex and mark it as visited
        current_vertex = v
        (self.Vertices[v]).visited = True
        the_queue.enqueue(current_vertex)

        # visit all the other vertices according to breadth
        while not (the_queue.is_empty()):

            # set the current vertex and print it out
            current_vertex = the_queue.dequeue()
            print(self.Vertices[current_vertex])

            # find the neighbors of the current vertex
            vertex_neighbors = self.get_neighbors(self.Vertices[current_vertex].get_label())

            # insert all of the neighbors of the current vertex that have not been visited
            # into the queue
            for vertex in vertex_neighbors:
                if (self.Vertices[vertex].was_visited() == False):
                    the_queue.enqueue(vertex)
                    self.Vertices[vertex].visited = True

        # the queue is empty, reset the flags
        num_vertices = len(self.Vertices)
        for i in range(num_vertices):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge(self, fromVertexLabel, toVertexLabel):

        # find the respective indices of the two labels
        label1_index = self.get_index(fromVertexLabel)
        label2_index = self.get_index(toVertexLabel)

        # delete a single edge
        if (self.get_edge_weight(fromVertexLabel, toVertexLabel) != 0):
            self.adjMat[label1_index][label2_index] = 0

        # delete the second edge if necessary
        if (self.get_edge_weight(toVertexLabel, fromVertexLabel) != 0):
            self.adjMat[label2_index][label1_index] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):

        # if the vertex is not in the list of vertices, do nothing
        if not self.has_vertex(vertexLabel):
            return

        # remove the vertex from the list of vertices
        vertex_index = self.get_index(vertexLabel)
        self.Vertices.pop(vertex_index)

        # remove the vertex row
        del self.adjMat[vertex_index]

        # remove the vertex column
        for row in range(len(self.adjMat)):
            del self.adjMat[row][vertex_index]

    # prints the adjacency matrix in the correct format
    def print_adjacency_matrix(self):

        # find the ranges
        i = len(self.adjMat)
        j = len(self.adjMat[0])

        # iterate through the adjacency matrix and print the values
        for row in range(i):
            for col in range(j - 1):
                print(self.adjMat[row][col], end = ' ')
            print(self.adjMat[row][j - 1])

def main():

    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_vertex(city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])
        cities.add_directed_edge(start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # do the depth first search
    print ("Depth First Search")
    cities.dfs(start_index)
    print ()

    # do the breadth first search
    print ("Breadth First Search")
    cities.bfs(start_index)
    print ()

    # read the edge to be deleted
    line = sys.stdin.readline().strip()
    two_cities = line.split()

    # delete the edge between the two cities
    print('Deletion of an edge')
    cities.delete_edge(two_cities[0], two_cities[1])
    print()

    # print the adjacency matrix
    print('Adjacency Matrix')
    cities.print_adjacency_matrix()
    print()

    # read the city to be deleted
    city = sys.stdin.readline().strip()

    # delete the city and its edges
    print('Deletion of a vertex')
    cities.delete_vertex(city)
    print()

    # print the list of vertices
    print('List of Vertices')
    for vertex in cities.get_vertices():
        print(vertex)
    print()

    # print the adjacency matrix
    print('Adjacency Matrix')
    cities.print_adjacency_matrix()

if __name__ == "__main__":
    main()