import unittest

# Use the imports below to test either your array-based stack
# or your link-based version

from stack_array import Stack
# from stack_linked import Stack


class TestLab2(unittest.TestCase):

    def test_stack(self):
        # test the init method
        s_1 = Stack(5)
        s_2 = Stack(10)

        # left is expected, right is what we want the thing to be on the left
        # self.assertEqual(expected: 13, actual: 6 + 7)
        self.assertEqual(5, s_1.capacity)
        self.assertEqual(0, s_1.num_items)

        self.assertEqual(10, s_2.capacity)
        self.assertEqual(0, s_2.num_items)

    def test_is_empty(self):

        # create a stack
        s_1 = Stack(1)

        # test to see if is_empty returns true
        self.assertTrue(s_1.is_empty())
        # add something to the stack
        s_1.push("NotEmpty")
        # test to see if is_empty returns false
        self.assertFalse(s_1.is_empty())

    def test_is_full(self):

        # create a stack
        s_1 = Stack(2)

        # test to see if is_full returns false
        self.assertFalse(s_1.is_full())
        # add one item (dont fill it) (uses push)
        s_1.push("Full")
        # test to see if it still returns false
        self.assertFalse(s_1.is_full())

        # fill it (uses push)
        s_1.push("Stack")
        # test to see if it returns true
        self.assertTrue(s_1.is_full())

    def test_push(self):
        # create a stack
        s_1 = Stack(1)
        # If stack is not full make sure push works

        s_1.items = [None]
        s_1.push("A")
        s_1.items = ["A"]

        self.assertEqual("A", s_1.peek())

        # test to see it returns IndexError when full
        with self.assertRaises(IndexError):
            s_1.push("")

    def test_pop(self):
        # create a stack
        # since s1 is one instance of a Class Stack it is an object

        s_1 = Stack(1)

        s_2 = Stack(2)

        # check if its empty and raises exception
        with self.assertRaises(IndexError):
            s_1.pop()

        # object on method
        # if not empty check return pop_del var
        s_1.push("B")

        # s_2.items = [None, None]
        s_2.push("C")
        s_2.push("&")
        # s_2.items = ["C", None]

        # using the method on the object
        self.assertEqual("B", s_1.pop())
        self.assertEqual("&", s_2.pop())

        # make sure the item got removed
        self.assertEqual(0, s_1.num_items)
        self.assertEqual(1, s_2.num_items)

    def test_peek(self):
        # create a stack
        s_1 = Stack(1)
        s_2 = Stack(2)

        # check if its empty and raises exception
        with self.assertRaises(IndexError):
            s_1.pop()

        s_1.push("D")
        s_2.push("3")
        s_2.push("$")

        # using the method on the object
        self.assertEqual("D", s_1.peek())
        self.assertEqual("$", s_2.peek())

        # make sure the item didn't get removed
        # if we run pop twice it should give dif results but peek twice same results
        self.assertEqual("D", s_1.peek())
        self.assertEqual("$", s_2.peek())

    def test_size(self):

        # create a stack
        s_1 = Stack(1)
        self.assertEqual(0, s_1.size())
        # push an element into stack
        s_1.push("1")
        # check to see if an element matches
        self.assertEqual(1, s_1.size())
        # check pop
        s_1.pop()
        # check if element is removed
        self.assertEqual(0, s_1.size())


if __name__ == '__main__': 
    unittest.main()
