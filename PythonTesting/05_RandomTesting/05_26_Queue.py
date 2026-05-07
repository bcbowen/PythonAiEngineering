# TASK:
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call 
# the Queue methods on random input in a 
# semi-random fashion. for instance, if 
# you wanted to randomly decide between 
# calling enqueue and dequeue, you would 
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call the enqueue, dequeue, 
# and checkRep methods several thousand 
# times each.

import array
import random

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

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)

# Write a random tester for the Queue class.
def test():
    def get_next_op(): 
        return random.randint(0, 1)
    def get_next_value(): 
        return random.randint(0, 2000)
    def get_next_capacity(): 
        return random.randint(100, 2000)
    
    e_count = 0
    d_count = 0
    for i in range(1000): 
        items = []
        capacity = get_next_capacity()
        q = Queue(capacity)

        for j in range(1000): 
            next_op = get_next_op() 
            if next_op == 0: 
                # enqueue
                next_val = get_next_value() 
                result = q.enqueue(next_val)
                
                if result: 
                    e_count += 1
                    items.append(next_val)
                else: 
                    # The queue thinks it's full
                    assert(len(items) == capacity)
                    assert(q.full())
                q.checkRep()
            else: 
                # dequeue
                val = q.dequeue()
                
                if val != None:
                    d_count += 1 
                    assert(val == items[0])
                    items.pop(0)
                else: 
                    assert(len(items) == 0)
                    assert(q.empty())

    print(f"{e_count} enqueues; {d_count} dequeues")


test()