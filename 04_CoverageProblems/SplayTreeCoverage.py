# TASK:
#
# This is the SplayTree code we saw earlier in the 
# unit. We didn't achieve full statement coverage 
# during the unit, but we will now!
# Your task is to achieve full statement coverage 
# on the SplayTree class. 
# 
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you 
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the 
#    entire code base.
#
# You can also run your code through a code coverage 
# tool on your local machine if you prefer. This is 
# not necessary, however.
# If you have any questions, please don't hesitate 
# to ask in the forums!

from typing import Optional

class Node:
    def __init__(self, key):
        self.key = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def equals(self, node):
        return self.key == node.key

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None) #For splay()

    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
            return

        self.splay(key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        n = Node(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if self.root is None or key != self.root.key:
            return

        # Now delete the root.
        if self.root.left== None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None
    
    def splay(self, key):
        l = r = self.header
        t = self.root
        if t is None:
            return
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t


# Write test code in this function to achieve 
# full statement coverage on the SplayTree class.
def test():
    test_new_tree_has_null_root()
    test_insert_empty_tree()
    test_insert_dupe()
    test_insert_smaller_val_replaces_root()
    test_insert_larger_val_replaces_root()
    test_remove_from_empty_tree()
    test_remove_nonexistent_node()
    test_remove_with_no_left_node()
    test_remove_with_left_and_right_nodes()
    test_find_min_empty_tree()
    test_find_min()
    test_find_max_empty_tree()
    test_find_max()
    test_find_empty_tree()
    test_find_existing_value()
    test_find_nonexisting_value()
    test_is_empty_true()
    test_is_empty_false() 


def test_new_tree_has_null_root(): 
    t = SplayTree(); 
    assert(t.root == None)

def test_insert_empty_tree(): 
    t = SplayTree()
    t.insert(1)
    assert(t.root != None)
    assert(t.root.key == 1)

def test_insert_dupe(): 
    t = SplayTree()
    t.insert(1)
    t.insert(1)
    assert(t.root != None)
    assert(t.root.key == 1)

def test_insert_smaller_val_replaces_root(): 
    t = SplayTree()
    t.insert(10)
    t.insert(15)
    t.insert(5)
    assert(t.root != None)
    assert(t.root.key == 5)
    assert(t.root.left == None)
    assert(t.root.right != None)
    assert(t.root.right.key == 10)
    

def test_insert_larger_val_replaces_root(): 
    t = SplayTree()
    t.insert(15)
    t.insert(10)
    t.insert(20)
    assert(t.root != None)
    assert(t.root.key == 20)
    assert(t.root.left != None)
    assert(t.root.left.key == 15)
    assert(t.root.right == None)
    
def test_remove_from_empty_tree(): 
    t = SplayTree() 
    t.remove(8)
    assert(t.root == None)

def test_remove_nonexistent_node():
    t = SplayTree()
    t.insert(3) 
    t.remove(8)
    assert(t.root != None)
    assert(t.root.key == 3)

def test_remove_with_no_left_node(): 
    t = SplayTree() 
    t.insert(5)
    t.insert(8)
    t.remove(5)
    assert(t.root != None)
    assert(t.root.key == 8) 

def test_remove_with_left_and_right_nodes(): 
    t = SplayTree() 
    for i in range(10): 
        t.insert(i)

    t.remove(4)
    assert(t.root != None)
    assert(t.root.key == 3)
    assert(t.root.left != None)
    assert(t.root.right != None)
    
def test_find_min_empty_tree(): 
    t = SplayTree() 
    result = t.findMin() 
    assert(result == None)

def test_find_min(): 
    t = SplayTree() 
    for i in range(9): 
        t.insert(i)
        t.splay(5)
    result = t.findMin()
    assert(result == 0) 
    assert(t.root != None)
    assert(t.root.key == 0)

def test_find_max_empty_tree(): 
    t = SplayTree() 
    result = t.findMax() 
    assert(result == None)

def test_find_max(): 
    t = SplayTree() 
    for i in range(9): 
        t.insert(i)
        t.splay(5)
    result = t.findMax()
    assert(result == 8) 
    assert(t.root != None)
    assert(t.root.key == 8)

def test_find_empty_tree(): 
    t = SplayTree() 
    result = t.find(3) 
    assert(result == None)

def test_find_existing_value():
    t = SplayTree() 
    for i in range(9): 
        t.insert(i)
        t.splay(5)
    val = 4
    result = t.find(val)
    assert(result == val)
    assert(t.root != None)
    assert(t.root.key == val)

def test_find_nonexisting_value(): 
    t = SplayTree() 
    for i in range(9): 
        t.insert(i)
        t.splay(5)
    result = t.find(23)
    assert(result == None)

def test_is_empty_true():
    t = SplayTree()
    assert(t.isEmpty()) 

def test_is_empty_false():
    t = SplayTree()
    t.insert(4)
    assert(not t.isEmpty()) 

test()

