
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.size = 0
        self.Heap = [None]

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        if self.size + 1 > self.capacity: return False
        self.Heap.append(item)
        self.size += 1
        self.perc_up(self.size) # self.size will be the last index in the heap.
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.size: return self.Heap[1]
        return False

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        if self.size == 0: return None
        elif self.size == 1:
            self.size -= 1
            return self.Heap.pop(1)
        else:
            self.size -= 1 # decrement size
            self.swap(1, -1) # swap first and last element
            popped = self.Heap.pop() # pop the last element
            self.perc_down(1) # perc down on the new first element
            return popped

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.Heap[1:]

    def build_heap(self, alist):
        # alist = [2,1,3] self.Heap = [None, 2,1,3]
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist'''
        self.Heap = [None]  # first value will be None so we can find the parent using (idx//2)
        # idx 1 will be the root as 1//2 = 0. idx 2 is 2//2 = 1. idx 3 is 3//2 = 1.
        self.size = len(alist)
        if self.size > self.capacity: self.capacity = self.size
        ''' TOP DOWN APPROACH '''
        # for index, element in enumerate(alist):
        #     self.Heap.append(element)
        #     self.perc_up(index+1) # needs to be plus 1 because our self.Heap doesn't start at index 0, but index 1.
        ''' BOTTOM UP APPROACH '''
        startIdx = (self.size//2-1)+1  # gives us the index of last non-leaf node in our array (heap) also adding 1 to account for None buffer
        self.Heap += list(alist)
        for i in range(startIdx, 0, -1): # going backwards from starIdx to 1 (0 is not included since it's None) (checking all the heaps)
            self.perc_down(i)

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.size == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.size == self.capacity
        
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size
        
    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        left = i * 2
        right = (i * 2) + 1
        largest = i
        if self.size >= left and self.Heap[largest] < self.Heap[left]:
            largest = left # if left exists, and the left child is bigger than the current node (its parent)...
        if self.size >= right and self.Heap[largest] < self.Heap[right]:
            largest = right # if right exists, and right is bigger than largest (largest could be i or left remember?)...
        if largest != i: # if largest not i (node we are evaluating), then swap with left/right.
            self.swap(i, largest)
            self.perc_down(largest) # now i is in parent position, and repeat the check.

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        parent = i // 2
        if i <= 1: return # if index is just 1, there is only 1 element (excluding placeholder "None") so no need to do anything
        elif self.Heap[i] > self.Heap[parent]: # if node is greater than parent
            self.swap(i, parent) # swap with parent
            self.perc_up(parent) # now i is in the parent position, and repeat the check.

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        # https://stackoverflow.com/questions/41212072/ascending-and-descending-heapsort
        self.build_heap(alist)
        for i in range(len(alist)-1, -1, -1): # return the max value and insert into alist backwards to get ascending order.
            alist[i] = self.dequeue()


    '''Helper Functions'''
    def swap(self, i, j):
        self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]
