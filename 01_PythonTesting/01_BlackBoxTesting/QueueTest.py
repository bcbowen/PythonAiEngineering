import array

# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.


#from queue_test import *

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

"""
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#

"""
def test():
    one_test()
    two_test()
    big_test()
    int32_test()
    neg_test()

def one_test():
    q = init_queue(1)

    result = q.enqueue(10)
    assert(not q.empty())
    assert(result)
    #assert(q.size == 1)
    assert(q.full())

    result = q.enqueue(11)
    assert(not result)
    assert(q.full())

    
    result = q.dequeue()
    assert(result == 10)
    assert(q.empty())
    assert(not q.full())
    #assert(q.size == 0)

def two_test():
    q = init_queue(2)
    q.enqueue(10)
    assert(not q.empty())
    assert(not q.full())

    q.enqueue(11)
    assert(q.full())

    result = q.enqueue(99)
    assert(not result)

    result = q.dequeue()
    assert(result == 10)
    assert(not q.empty())
    assert(not q.full())

    q.enqueue(12)
    assert(q.full())
    
    result = q.dequeue()
    assert(result == 11)

    result = q.dequeue()
    assert(result == 12)

    assert(q.empty())    

def big_test(): 
    n = 128
    q = init_queue(n)
    for i in range(n): 
        q.enqueue(i)
    
    for i in range(n): 
        val = q.dequeue()
        assert(val == i)

def neg_test(): 
    q = init_queue(1)
    q.enqueue(-1)
    val = q.dequeue() 
    assert(val == -1)

def int32_test(): 
    q = init_queue(1)
    val = 2_147_483_647
    q.enqueue(val)
    result = q.dequeue()
    assert(result == val) 
                       

def init_queue(n): 
    q = Queue(n)
    assert(q.empty())
    assert(not q.full())  
    result = q.dequeue()
    assert(result == None)
    return q


if __name__ == "__main__":
    test() 