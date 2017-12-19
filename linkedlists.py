"""Linked Lists"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.current_node = None

    def add_node(self, data):
        new = Node()
        new.data = data
        new.next = self.current_node #current_node.data and current_node.next exist

        self.current_node = new

    def print_list(self):
        pnode = self.current_node
        while pnode:
            print(pnode.data)
            pnode = pnode.next

    def get_next(self):
        pass

'''
    def insert_node(self, data, position):
        new = Node()
        new.data = data
        new.next
'''

l = LinkedList()
l.add_node(1)
l.add_node(2)
l.add_node(3)
l.print_list()
