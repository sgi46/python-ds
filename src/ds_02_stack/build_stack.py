'''
Stack is user-defined data structure created using list, stack has its unique propery.

Stack works in LIFO (Last In, First Out) way

Item which enters last, will leave the stack data structure first.

Stack is recommended for Last In, First Out operation (i.e. append() at last and pop() at last). 
Stack is not efficient for Adding items in first and removing items in the front.

It is suggested to use Queue or Deque Data Structure which allows inserting and deleting the elements
in the front
'''
class Stack():

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)

        if not self.min_stack or self.min_stack[-1]>item:
            self.min_stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        val = self.stack.pop() 
        if val==self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack.clear()

    def size(self):
        return len(self.stack)

    def to_string(self):
        return "".join(self.stack)

    def find_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

    def __iter__(self):
        return iter(self.stack)

    def __str__(self):
        return str(self.stack)

