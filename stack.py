# Stack Data Structure in implementation using lists
# Stack is a LIFO - Last in, first out Data structures

# Python lists, pop method, takes item at the end of the list
# Python lists, append method, pushs item at the end of the list

class Stack:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def pop(self):
        return self.items.pop()

    # Need item to push 
    def push(self, item):
        self.items.append(item)
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack() 

s.push(1)
s.push(100)

print(s.peek())

s.pop()

print(s.peek())
    
    