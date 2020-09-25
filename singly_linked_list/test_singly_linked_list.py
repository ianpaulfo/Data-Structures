# class Node:
#   def __init__(self, value=None, next_node=None):
#     self.value = value
#     self.next_node = next_node
#   def get_value(self):
#     return self.value
#   def get_next(self):
#     return self.next_node
#   def set_next(self, new_next):
#     self.next_node = new_next
    
# class LinkedList:
#   def __init__(self):
#     self.head = None
#     self.tail = None

#   def add_to_head(self, value):
#     new_node = Node(value)
#     if not self.head and not self.tail:
#       self.head = new_node
#       self.tail = new_node
#     else:
#       new_node.set_next(self.head)
#       self.head = new_node

#   def add_to_tail(self, value):
#     new_node = Node(value, None)
#     if not self.head:
#       self.head = new_node
#       self.tail = new_node
#     else:
#       self.tail.set_next(new_node)
#       self.tail = new_node

#   def remove_head(self):
#     if not self.head:
#       return None
#     if not self.head.get_next():
#       head = self.head
#       self.head = None
#       self.tail = None
#       return head.get_value()
#     value = self.head.get_value()
#     self.head = self.head.get_next()
#     return value

#   # def remove_tail(self):
#     # if not self.head and not self.tail:
#     #   return None
#     # if self.head == self.tail:
#     #         self.head = None
#     #         self.tail = None

#   def contains(self, value):
#     if not self.head:
#       return False
#     current = self.head
#     while current:
#       if current.get_value() == value:
#         return True
#       current = current.get_next()
#     return False

#   def get_max(self):
#     if not self.head:
#       return None
#     current = self.head
#     max_val = self.head.get_value()
#     while current:
#       if current.get_value() > max_val:
#         max_val = current.get_next()
#       current = current.get_next()
#     return max_val 



# import unittest
# from singly_linked_list import LinkedList

# class LinkedListTests(unittest.TestCase):
#     def setUp(self):
#         self.list = LinkedList()

#     def test_add_to_tail(self):
#         self.list.add_to_tail(1)
#         self.assertEqual(self.list.tail.value, 1)
#         self.assertEqual(self.list.head.value, 1)
#         self.list.add_to_tail(2)
#         self.assertEqual(self.list.tail.value, 2)
#         self.assertEqual(self.list.head.value, 1)

#     def test_contains(self):
#         self.list.add_to_tail(1)
#         self.list.add_to_tail(2)
#         self.list.add_to_tail(5)
#         self.list.add_to_tail(10)
#         self.assertTrue(self.list.contains(10))
#         self.assertTrue(self.list.contains(2))
#         self.assertFalse(self.list.contains(1000))

#     def test_remove_head(self):
#         self.list.add_to_tail(10)
#         self.list.add_to_tail(20)
#         self.assertEqual(self.list.remove_head(), 10)
#         self.assertFalse(self.list.contains(10))
#         self.assertEqual(self.list.remove_head(), 20)
#         self.assertFalse(self.list.contains(20))

#         self.list.add_to_tail(10)    
#         self.assertEqual(self.list.remove_head(), 10)    
#         self.assertIsNone(self.list.head)
#         self.assertIsNone(self.list.tail)
#         self.assertIsNone(self.list.remove_head())

#     def test_get_max(self):
#         self.assertIsNone(self.list.get_max())
#         self.list.add_to_tail(100)
#         self.assertEqual(self.list.get_max(), 100)
#         self.list.add_to_tail(55)
#         self.assertEqual(self.list.get_max(), 100)
#         self.list.add_to_tail(101)
#         self.assertEqual(self.list.get_max(), 101)

# if __name__ == '__main__':
#     unittest.main()




import unittest
from singly_linked_list import LinkedList

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_add_to_tail(self):
        self.list.add_to_tail(1)
        self.assertEqual(self.list.tail.value, 1)
        self.assertEqual(self.list.head.value, 1)
        self.list.add_to_tail(2)
        self.assertEqual(self.list.tail.value, 2)
        self.assertEqual(self.list.head.value, 1)

    def test_remove_head(self):
        self.list.add_to_tail(10)
        self.list.add_to_tail(20)
        self.assertEqual(self.list.remove_head(), 10)
        self.assertEqual(self.list.remove_head(), 20)

        self.list.add_to_tail(10)    
        self.assertEqual(self.list.remove_head(), 10)    
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertIsNone(self.list.remove_head())

    def test_remove_tail(self):
        self.list.add_to_tail(30)
        self.list.add_to_tail(40)
        self.assertEqual(self.list.remove_tail(), 40)
        self.assertEqual(self.list.remove_tail(), 30)

        self.list.add_to_tail(100)    
        self.assertEqual(self.list.remove_tail(), 100)    
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertIsNone(self.list.remove_tail())

if __name__ == '__main__':
    unittest.main()