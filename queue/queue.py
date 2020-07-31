class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  def get_value(self):
    return self.value
  def get_next(self):
    return self.next_node
  def set_next(self, new_next):
    self.next_node = new_next
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_head(self, value):
    new_node = Node(value)
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.set_next(self.head)
      self.head = new_node

  def add_to_tail(self, value):
    new_node = Node(value, None)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    if not self.head:
      return None
    if not self.head.get_next():
      head = self.head
      self.head = None
      self.tail = None
      return head.get_value()
    value = self.head.get_value()
    self.head = self.head.get_next()
    return value

  # def remove_tail(self):
    # if not self.head and not self.tail:
    #   return None
    # if self.head == self.tail:
    #         self.head = None
    #         self.tail = None

  def contains(self, value):
    if not self.head:
      return False
    current = self.head
    while current:
      if current.get_value() == value:
        return True
      current = current.get_next()
    return False

  def get_max(self):
    if not self.head:
      return None
    current = self.head
    max_val = self.head.get_value()
    while current:
      if current.get_value() > max_val:
        max_val = current.get_next()
      current = current.get_next()
    return max_val 

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# import sys
# sys.path.append('../singly_linked_list')
# from singly_linked_list import LinkedList

class ArrayQueue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def __len__(self):
    return len(self.storage)

  def enqueue(self, value):
    self.storage.append(value)

  def dequeue(self):
    if len(self.storage) == 0:
      return None
    return self.storage.pop(0)

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
          return None
        self.size -= 1
        self.storage.remove_head()