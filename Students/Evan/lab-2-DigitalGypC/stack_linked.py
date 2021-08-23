class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This is how to add to the beginning (push), doesnt work if full, different if empty b/c self.head is None
# self.head = Node(5, None)
# self.head = Node(new_value, Node(self.head.value (only if self.head is not None), self.head.next
# (only if self.head is not none))

# This is how to remove from the head (pop), doesnt work if empty
# saved_value = self.head.data
# self.head = self.head.next


# anytime it accesses items in stack array cant use here
class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Linked List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.head = None
        self.num_items = 0

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

        if self.num_items == self.capacity:
            raise IndexError

        else:
            if self.head is None:
                self.head = Node(item)
            else:
                new_node = Node(item)
                new_node.next = self.head
                self.head = new_node
            self.num_items += 1

    # pop pulls from top and removes from the top
    def pop(self):
        """If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance


        Returns:
            item: pops item from stack and returns item

        Raises:
            IndexError: "Stack is Empty"

        """
        # If stack is empty when pop is attempted, raises IndexError
        if self.is_empty():
            raise IndexError
        # not empty, pops item from stack and returns item.
        else:
            pop_sav = self.head.data
            self.head = self.head.next
            self.num_items -= 1
            return pop_sav

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
        if self.is_empty():
            raise IndexError
        else:
            return self.head.data

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance

        Returns:
            int: number of elements in stack (not capacity)
       """
        return self.num_items
