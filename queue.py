# Queue Data Structure in implementation using lists
# Queue is a FIFO - First in, first out Data structures

# Python lists, pop method, takes item at the end of the list
# Python lists, append method, pushs item at the end of the list

# 0 is the first one in
# length of list is last one in

class Queue:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

q = Queue()

q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())



