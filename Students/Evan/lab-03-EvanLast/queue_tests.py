import unittest
from queue_array import Queue
from queue_linked import Queue


class TestLab1(unittest.TestCase):
    def test_queue(self):
        """Trivial test to ensure method names and parameters are correct"""
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()
        # test the init method
        self.assertEqual(5, q.capacity)
        self.assertEqual(0, q.num_items)

    def test_is_empty(self):
        q_1 = Queue(1)

        # test to see if is_empty returns true
        self.assertTrue(q_1.is_empty())
        # add something to the Queue
        q_1.enqueue("NotEmpty")
        # test to see if is_empty returns false
        self.assertFalse(q_1.is_empty())

    def test_is_full(self):
        # create a stack
        q_1 = Queue(2)

        # test to see if is_full returns false
        self.assertFalse(q_1.is_full())
        # add one item (dont fill it) (uses push)
        q_1.enqueue("Full")
        # test to see if it still returns false
        self.assertFalse(q_1.is_full())

        # fill it (uses push)
        q_1.enqueue("Queue")
        # test to see if it returns true
        self.assertTrue(q_1.is_full())

    def test_enqueue(self):
        q_1 = Queue(1)
        q_2 = Queue(2)

        q_1.enqueue("A")
        self.assertEqual(1, q_1.size())

        # check if its not empty
        # Node( 1, Node(1, None))
        q_2.enqueue("B")
        q_2.enqueue("C")
        self.assertEqual(2, q_2.size())

        # test to see it returns IndexError when full
        with self.assertRaises(IndexError):
            q_1.enqueue("")

    def test_dequeue(self):
        # create a Queue
        # since q1 is one instance of a Class Queue it is an object

        q_1 = Queue(1)

        q_2 = Queue(2)

        # check if its empty and raises exception
        with self.assertRaises(IndexError):
            q_1.dequeue()

        # object on method
        # if not empty check return deq_var var
        q_1.enqueue("B")

        # s_2.items = [None, None]
        q_2.enqueue("C")
        q_2.enqueue("&")
        # s_2.items = ["C", None]

        # using the method on the object
        self.assertEqual("B", q_1.dequeue())
        self.assertEqual("C", q_2.dequeue())

        # make sure the item got removed
        self.assertEqual(0, q_1.num_items)
        self.assertEqual(1, q_2.num_items)

    def test_size(self):
        # create a Queue
        q_1 = Queue(1)
        self.assertEqual(0, q_1.size())
        # push an element into Queue
        q_1.enqueue("1")
        # check to see if an element matches
        self.assertEqual(1, q_1.size())
        # check pop
        q_1.dequeue()
        # check if element is removed
        self.assertEqual(0, q_1.size())

    def test_dequeue_1(self):
        # create a Queue
        # since q1 is one instance of a Class Queue it is an object

        q_1 = Queue(4)

        q_2 = Queue(2)

        # check if its empty and raises exception


        # object on method
        # if not empty check return deq_var var


        # s_2.items = [None, None]
        q_1.enqueue("3")
        q_1.enqueue("9")
        q_1.enqueue("7")
        q_1.enqueue("8")
        q_1.dequeue()
        q_1.dequeue()
        q_1.enqueue("5")
        q_1.enqueue("6")
        q_1.dequeue()
        # s_2.items = ["C", None]
        self.assertEqual(1, q_1)
        print(q_1)
        # using the method on the object






if __name__ == '__main__': 
    unittest.main()
enqueue(3),  enqueue(9),  enqueue(7),  enqueue(8) , dequeue(),  dequeue(), enqueue(5), enqueue(6), dequeue()
3, 9, 7, 8
9, 7, 8
7,8
7, 8 5
7, 8, 5 ,6
8, 5, 6


q3
push(3),  push(9),  push(7),  push(8) , pop(),  pop(), push(5), push(6), pop()

3
3, 9
3, 9, 7
3, 9, 7, 8
3, 9, 7
3, 9
3, 9, 5
3, 9, 5, 6
3, 9, 5
