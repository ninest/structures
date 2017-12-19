class Stack:
    def __init__(self, size):
        self.list = []
        self.size = size

    def push(self, value):
        if len(self.list) <= self.size:
            self.list.append(value)
        else:
            print('stack full')
            #raise Exception('Stack is full')

    def pop(self):
        if not self.is_empty():
            self.list.pop()
        else:
            print('stack empty')
            # raise Exception('stack empty')

    #nomber of elements in stack
    def no_elements(self):
        return len(self.list) - 1

    def top(self):
        if not self.is_empty():
            #print(self.list[self.size - 1])
            return self.list[self.no_elements()]
        else:
            print('stack empty')
            # raise Exception('stack empty')

    def is_empty(self):
        return not bool(self.list)

    def get_stack(self):
        return self.list
        #print("\nSTACK:")
        #for i in self.list:
        #    print(i)

    def add_list(self, *args):
        for a in args:
            if len(self.list) <= self.size:
                self.list.append(a)
            else:
                print('stack full')

s = Stack(30)
s.add_list(1,2,3,4,5,6,7,8,91,2,3)
s.push(1)
s.push(2)

print('stack size: ', s.size)
print("top: ", s.top())
print("number of elements: ", s.no_elements())
print('stack: ', s.get_stack())

