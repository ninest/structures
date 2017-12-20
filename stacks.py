class Stack:
    """First in, last out; last element is at top of list (first element while being printed"""
    # sds

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return not bool(self.stack)

    def display(self):
        r_list = []
        for item in reversed(self.stack):
            r_list.append(item)

        print(r_list)

        
# Example:
s = Stack()
print(s.is_empty())

s.push(1)
s.push(4)
s.push(5)
s.push(2)
s.push(8)

s.pop()

print(s.is_empty())
s.display()
