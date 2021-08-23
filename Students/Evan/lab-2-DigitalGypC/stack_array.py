"""
Assignment: lab 2 & Project 2


Repository: CalPolyCPE/cpe202_project_2/Project-2

Name: Evan Last

Cal Poly User: ebsahagu
"""


'''
Stack LIFO ie. add to top remove from top
Queue FIFO 
'''
class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.items = [None] * capacity

        # num_items points to the first empty slot in the stack array
        self.num_items = 0

    def __repr__(self):
        return f'Stack({self.capacity}, {self.num_items}, {self.items})'

    def is_empty(self):
        """ Returns True if the stack is empty, and False otherwise
            MUST have O(1) performance

        Returns:
            bool: True for empty, False otherwise

        """
        # 4 Function Template
        # if num_items == 0
        # return True
        # else
        # return False

        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self):
        """Returns True if the stack is full, and False otherwise
           MUST have O(1) performance

        Returns:
            bool: True for full, False for otherwise

        """
        # 4 Function Template
        # if num_items == capacity:
        # return True
        # else:
        # return False

        if self.num_items == self.capacity:
            return True
        else:
            return False

    def push(self, item):
        """If stack is not full, pushes item on stack.
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance
           # O(1) dont use loops

        Args:
            item: something in the stack (ie a pancake in a stack of pancakes)

        Raises:
            IndexError: stack is full and push is attempted

        """
        # 4 Function Template
        # if not self.is_full():
        # item is what we are adding to self.items in the correct spot
        # num_items is first place to add to list
        # num_items minus 1 is the index of the previous item

        if self.is_full():
            raise IndexError
        else:  # stack is not full
            #
            self.items[self.num_items] = item  # i.e. items[0] = 5
            self.num_items += 1

    # pop pulls from top and removes from the top
    def pop(self):
        """If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance

        Returns:
            item: pops item from stack and returns item that got popped

        Raises:
            IndexError: "Stack is Empty"

        """
        # If stack is empty when pop is attempted, raises IndexError
        if self.is_empty():
            raise IndexError

        # If stack is not empty, pops item from stack and returns item.
        else:
            # save
            pop_del = self.items[self.num_items-1]

            # delete
            self.items[self.num_items-1] = None

            self.num_items -= 1

            return pop_del

    # peek looks at the top but does not remove
    def peek(self):
        """If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance

        Returns:
            item: the top item (but does not remove item)

        Raises:
            IndexError: "Stack is Empty"

        """

        # If stack is empty when peek is attempted, raises IndexError
        if self.is_empty():
            raise IndexError

        # If stack is not empty, peek item from stack and returns item.
        else:
            return self.items[self.num_items - 1]

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance

        Returns:
            int: number of elements in stack (not capacity)

       """
        return self.num_items


