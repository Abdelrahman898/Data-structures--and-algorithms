
# Stack

class Stack:
    def __init__(self):
        self.items = []
        
    # insert the element at the end of the stack
    def push(self, value):
        self.items.append(value)
    
    # remove the element at the end of the stack
    def pop(self):
        if self.items is None:
            raise ValueError('Stack is empty')
        return self.items.pop()
    
    # check if the stack is empty
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    # return the top element
    def top(self):  
        if self.items is None:
            raise ValueError('Stack is empty')
        return self.items[-1]
    
    
stack = Stack()
stack.push(1)
stack.push(2)

print(stack.top())
print(stack.is_empty())


