
class Queue:
    """Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)"""

    def __init__(self, capacity):
        """Creates an empty Queue with a capacity"""
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0

        # we make queue with capacity 5 -> self.items = [None, None, None, None, None]
        # head and tail always start off at the beginning, so zero
        # head represents the first item in the queue (nothing right now, but normally not None)
        # tail represents the first empty position in the array (normally None)
        self.head = 0
        self.tail = 0

        # enqueue
        # if we add something, it ends up like this -> ['cat', None, None, None, None]
        # head = 0 still, but tail = 1

        # enqueue
        # let's add something else -> ['cat', 'dog', None, None, None]
        # head = 0 still, but tail = 2

        # dequeue
        # when we remove something, head needs to move
        # -> [None, 'dog', None, None, None]
        # head = 1, tail = 2

        # dequeue
        # if we remove again -> [None, None, None, None, None]
        # head = 2, tail = 2

        # enqueue
        # now if we add -> [None, None, 'poodle', None, None]
        # head = 2, tail = 3

        # 2x enqueue
        # (this needs to be done in two method calls) add two more -> [None, None, 'poodle', 'pip', 'fish']
        # head = 2, tail = 5 <- this is illegal, so we need to wrap it around
        # if head or tail == capacity, head or tail becomes zero
        # everytime we change head or tail, make sure that they dont go out of bounds
        # head = 2, tail = 0

        # enqueue
        # add one more -> ['cat', None, 'poodle', 'pip', 'fish']
        # head = 2, tail = 1

        # enqueue
        # get one more - > ['cat', 'mouse', 'poodle', 'pip', 'fish']
        # head = 2, tail = 2

        # is_empty, is_full
        # if head is pointing to a space that hold None, then the queue must be empty
        # if tail points to something that isn't none, the queue is full

    def is_empty(self) -> bool:
        """ checks if queue is empty
        Returns:
            bool: True if the Queue is empty, and False otherwise
        """
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        # 4 Function Template
        # if num_items == 0
        # return True
        # else
        # return False

        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        """Checks if queue is full
        Returns:
            bool:True if the Queue is full, and False otherwise
        """
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
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
        """Adds to queue
        Args:
            item: One item at time
            If Queue is not full, enqueues (adds) item to Queue
        Raises:
            IndexError: If Queue is full when enqueue is attempted

        """

        '''If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        # 4 Function Template (pseudo code)
        # if not self.is_full():
        # item is what we are adding to self.items in the correct spot
        # num_items is first place to add to list
        # num_items minus 1 is the index of the previous item

        if self.is_full():
            raise IndexError
        else:  # Queue is not full
            self.items[self.tail] = item  # i.e. items[0] = 5
            self.num_items += 1
            self.tail += 1
            if self.tail == self.capacity:
                self.tail = 0

    def dequeue(self):
        """ Takes away item from queue


        """
        """If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance"""
        if self.is_empty():
            raise IndexError

        # If stack is not empty, pops item from stack and returns item.
        else:
            deq_item = self.items[self.head]  # deq_item is on spot 15 in the circle
            self.items[self.head] = None  # 15's reference is now NONE
            self.num_items -= 1    # Number of items is now one less
            self.head += 1         # Head was 15, now it is 16
            if self.head >= self.capacity:
                self.head = 0
            return deq_item

    def size(self):
        """Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance"""
        return self.num_items





