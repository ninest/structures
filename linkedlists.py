class Node:
    def __init__(self, data=None):
        """data stores the data in the list and next does NOT store the data of the next list
           next stores the object of the next data (it stores a Node() object)"""

        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head

        print(current_node.next is not None)    # current_node.next stores a Node() object
        while current_node.next is not None:    # checking whether there is a next Node() object (it can be None)
            print('D: ', current_node.next is not None)
            current_node = current_node.next

        current_node.next = new_node

    def length(self):
        current_node = self.head
        total = 0

        while current_node is not None:
            total += 1
            current_node = current_node.next
            # will return none if it is the last node because it does point to anything

        return total

    def display(self):
        elements = []
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)

        print(elements)

    def get(self, index):   # index at which we want to check data
        if index >= self.length():
            print('ERROR')
            return None

        current_index = 0
        current_node = self.head

        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR")
            return None

        current_index = 0
        current_node = self.head

        while True:
            last_node = current_node
            current_node = current_node.next

            if current_index == index:
                last_node.next = current_node.next
                break

            current_index += 1


# EXAMPLE:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.display()

print(ll.get(2))

ll.erase(2)
ll.display()
