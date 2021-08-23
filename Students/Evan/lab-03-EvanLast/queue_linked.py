

# you want the head of the linked list to be the data you want to access the most
# As an example the data we want to deal with the most we access head.
# using tail bc needs to be in constant time
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Queue:
    """Implements an link-based ,efficient first-in first-out Abstract Data Type"""

    def __init__(self, capacity):
        """Creates an empty Queue with a capacity"""
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.num_items = 0

    def is_empty(self):
        """Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance"""
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
        """Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance"""
        # 4 Function Template
        # if num_items == capacity:
        # return True
        # else:
        # return False

        if self.num_items == self.capacity:
            return True
        else:
            return False

    def enqueue(self, item):
        """If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance"""

        if self.is_full():
            raise IndexError
        else:
            if self.head is None:  # create a head if it doesnt exist
                self.head = Node(item)

                # if there is only 1 item make sure head and tail point to the same.
                self.tail = self.head

                # Node(2, None) -> Node(2, Node(3, None))
            else:  # otherwise add to the back
                new_node = Node(item)
                self.tail.next = new_node
                self.tail = self.tail.next
            self.num_items += 1

    def dequeue(self):
        """If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance"""
        # If stack is empty when dequeue is attempted, raises IndexError
        if self.is_empty():
            raise IndexError
        # not empty, dequeues item from queue and returns item.
        else:
            # Node(1, None)
            deq_sav = self.head.data  # deq_sav = 1
            self.head = self.head.next  # self.head = None, self.tail = Node(1, None)
            self.num_items -= 1  # num_items = 0

            # check if empty then change tail
            if self.is_empty():
                self.tail = None  # self.head = None, self.tail = None

            return deq_sav

    def size(self):
        """Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance"""
        return self.num_items
