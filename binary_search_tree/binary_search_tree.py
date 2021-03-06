
# import sys
# sys.path.append('../stack')
# from stack import Stack


from collections import deque
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self:
            return
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if not self:
            return
        
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()
       

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        qq = deque()
        qq.append(self)

        while len(qq) >0:
            current = qq.popleft()
            print(current.value)
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        """[iterative PreOrder traversal]
        1- create an empty stack
        2- push the root node to the stack
        3- loop until the stack is empty
            1- pop the top element in the stack
            2- manipulate the popped node
            3- push the right node if it exists (push right first to have left on top)
            4- push the left node if it exists
            - repeat...
        """
        stack = []
        stack.append(self)
        while len(stack):
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        # s = []
        # s.append(node)
        # while s.len() > 0:
        #     t = s.pop()
        #     print(t.value)
        #     if t.right:
        #         s.push(t.right)
        #     if t.left:
        #         s.push(t.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

    def get_height(self):
        if self.left and self.right:
            return max(self.left.get_height(), self.right.get_height()) + 1
        if self.left:
            return self.left.get_height() + 1
        if self.right:
            return self.right.get_height() + 1
        else:
            return 0

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
