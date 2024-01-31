
# Queue

class Queue:
    def __init__(self):
        self.items = []
        
    # insert the element at the end of the queue
    def enqueue(self, value):
        self.items.append(value)
    
    # remove the element at the front of the queue
    def dequeue(self):
        if self.items is None:
            raise ValueError('Queue is empty')
        return self.items.pop(0)
    
    # check if the queue is empty
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    # return the front element
    def front(self):  
        if self.items is None:
            raise ValueError('Queue is empty')
        return self.items[0]
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)

print(queue.front())


