from stack_array import Stack #Needed for Depth First Search
from queue_array import Queue #Needed for Breadth First Search
from copy import deepcopy

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []

class Graph:
    '''Add additional helper methods if necessary.'''
        # helper functions
    @staticmethod # able to be called on class or object and ignores self or cls when called. Also a good use case is that it doesn't use class or instance data, but is still relevant to our class.
    def sort_vertices(vertices_list):
        return sorted(vertices_list, key=lambda x: int(x[1:]))
    
    @staticmethod
    def pop_from_stack_and_create_component(stack):
        component = []
        while stack.size():
            component.append(stack.pop())
        # reset stack values
        return component

    def push_to_stack(self, stack, vertex):
        if vertex.id not in stack.items:
            stack.push(vertex.id)  # only push the id, not the actual vertex object
        else:
            return
        for adj_v_id in vertex.adjacent_to: # DFS
            self.push_to_stack(stack, self.get_vertex(adj_v_id)) 

    def bfs_queue(self, vertices_at_lvl, queue, length, queue_copy):
        queue_items = list(filter(lambda items: items != None, queue_copy.items))
        # print([vertex.id for vertex in queue_items])
        for vertex in queue_items: # go through each vertex on a specific level (queue)
            for adj_v_id in vertex.adjacent_to: # check adjacent list for each vertex in queue
                # print("before if:", [vertex.id for vertex in queue_items])
                # print("adj_v_id:", adj_v_id)
                adj_vertex = self.get_vertex(adj_v_id)
                if adj_vertex in queue_items: return False # if any two vertices on same level are connected return false
                if adj_vertex not in queue_items and adj_vertex not in queue.items and adj_vertex not in queue_copy.items:
                    # print("before")
                    # print([vertex.id for vertex in list(filter(lambda items: items != None, queue.items))])
                    # print([vertex.id for vertex in list(filter(lambda items: items != None, queue_copy.items))])
                    queue.enqueue(adj_vertex) # if not, we can add it to our queue
                    queue_copy.enqueue(adj_vertex) # also add it to our queue copy
                    # print("after")
                    # print([vertex.id for vertex in list(filter(lambda items: items != None, queue.items))])
                    # print([vertex.id for vertex in list(filter(lambda items: items != None, queue_copy.items))])
        for _ in range(vertices_at_lvl): # dequeue from the queue copy so it only contains vertices on same level
            queue_copy.dequeue()
        if queue_copy.size() == 0: return True # if we have checked all the vertices in the component return True
        vertices_at_lvl = queue_copy.size() # gives us the # of vertices for the level we are on
        return self.bfs_queue(vertices_at_lvl, queue, length, queue_copy)
        
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.graph_d = {}
        with open(filename) as f: # with will automatically close the file
            for line in f:
                if line[-1] == "\n":
                    line = line[:-1]
                edge = line.split(" ")
                if edge[0] not in self.graph_d:
                    self.graph_d[edge[0]] = Vertex(edge[0])
                self.graph_d[edge[0]].adjacent_to.append(edge[1])
                    
                if edge[1] not in self.graph_d:
                    self.graph_d[edge[1]] = Vertex(edge[1])
                self.graph_d[edge[1]].adjacent_to.append(edge[0])

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.graph_d.keys():
            new_vertex = Vertex(key)
            new_vertex.id = key
            self.graph_d[key] = new_vertex

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.graph_d.keys():
            return self.graph_d[key]
        return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        if v2 not in self.graph_d[v1].adjacent_to:
            self.graph_d[v1].adjacent_to.append(v2)
        if v1 not in self.graph_d[v2].adjacent_to:
            self.graph_d[v2].adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        return self.sort_vertices(list(self.graph_d.keys()))

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        # each connected component will be a stack array
        vertices_ids = self.get_vertices()
        components = []
        stack = Stack(len(self.graph_d)) # create a new stack
        while vertices_ids:
            vertex = self.get_vertex(vertices_ids.pop(0)) # pop and grab first vertex to start
            self.push_to_stack(stack, vertex) # recursively push to stack using DFS
            component = self.pop_from_stack_and_create_component(stack) # pop and create component from stack
            component = self.sort_vertices(component) # sort component in ascending order
            components.append(component) # append componenet to components
            vertices_ids = [v_id for v_id in vertices_ids if v_id not in component] # reset vertices_ids with only ones that haven't been added to a stack
        components.sort(key=lambda c: c[0]) # sort components by first vertex
        return components


    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''

        components = self.conn_components()
        for component in components:
            vertex = self.get_vertex(component[0])   
            queue = Queue(len(component))
            queue_copy = deepcopy(queue)
            queue.enqueue(vertex) # push first vertex to queue
            queue_copy.enqueue(vertex) # push first vertex to queue
            if not self.bfs_queue(queue.size(), queue, len(component), queue_copy):
                return False
        return True
              
    
            

