import unittest
from graph import *
from queue_array import Queue

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
    
    def test_vertex(self):
        v = Vertex("v1")
        v.adjacent_to.append("v3")
        v.adjacent_to.append("v4")
        self.assertEqual(v.adjacent_to, ["v3","v4"])
        self.assertEqual(v.id, "v1")
    
    def test_sort_vertices(self):
        vertices = ["v3", "v1","v10","v5", "v9"] # testing case when vertex number goes up to double digits
        self.assertEqual(Graph.sort_vertices(vertices), ["v1", "v3","v5", "v9","v10"])

    def test_pop_from_stack_and_create_component(self):
        stack = Stack(10)
        stack.push("v1")
        stack.push("v4")
        stack.push("v10")
        component = Graph.pop_from_stack_and_create_component(stack)
        self.assertEqual(component, ['v10', 'v4', 'v1'])
        self.assertEqual(stack.items, [None, None, None, None, None, None, None, None, None, None])

    def test_push_to_stack(self):
        g = Graph('test2.txt')
        stack = Stack(10)
        v1 = Vertex("v1") # replacing v1 in the file with our new v1 vertex
        v1.adjacent_to.append("v6")
        g.push_to_stack(stack, v1)
        self.assertEqual(stack.items, ['v1', 'v6', 'v4', 'v7', 'v8', None, None, None, None, None])

    def test_bfs_queue(self):
        g = Graph('test2.txt')
        component = ["v1", "v2", "v3"]
        vertex = g.get_vertex(component[0])   
        queue = Queue(len(component))
        queue_copy = deepcopy(queue)
        queue.enqueue(vertex) # push first vertex to queue
        queue_copy.enqueue(vertex) # push first vertex to queue
        self.assertFalse(g.bfs_queue(queue.size(), queue, len(component), queue_copy))

    def test_graph_and_vertex_methods(self): #tests instance methods of our graph and vertex classes (not including helpers)
        g = Graph('test1.txt')
        v_id = "v10"
        g.add_vertex(v_id)
        new_vertex = g.get_vertex(v_id)
        self.assertEqual(new_vertex.id, v_id)
        g.add_edge("v10", "v1")
        self.assertTrue(g.is_bipartite())
        g.add_edge("v10", "v5")
        self.assertEqual(new_vertex.adjacent_to, ["v1", "v5"])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v10'], ['v6', 'v7', 'v8', 'v9']])
        self.assertFalse(g.is_bipartite())


if __name__ == '__main__':
   unittest.main()
