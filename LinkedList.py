# Singley Linked List implementation in Python

class Node:
    
    # Each node has data and a 'next', which points to the
    # next location of a node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    # Each Linked List contains a head
    def __init__(self):
        self.head = None
    
    # This method is used to insert new nodes at the head
    def push(self, new):
        
        node = Node(new)
        node.next = self.head
        self.head = node
    
    # This method is to insert nodes in the middle of the Linked List
    def insertAfter(self, prevNode, new):

        if prevNode is None:
            print('The previous node must be in the list')
            return

        # This is the new node
        newNode = Node(new) 

        # New node points to previous node's next node
        newNode.next = prevNode.next

        # previous node's next now points to the new node
        prevNode.next = newNode
    
    def append(self, new):

        #Create a new node with the new data
        newNode = Node(new)

        # If the list is empty, then make the new node the head
        if self.head is None:
            self.head = newNode
            return

        # Traverse through the whole Linked List 
        last = self.head
        while (last.next):
            last = last.next

        # Make the newNode the tail node 
        last.next = newNode

    # Delete node based on key
    def deleteNode(self, data):

        # Assign a temp variable pointing to the head of the list
        temp = self.head
        
        # Check if the head contains the data
        if (temp is not None):
            if (temp.data == data):
                self.head = temp.next
                temp = None
                return
        
        while (temp is not None):
            if (temp.data == data):
                break
            prev = temp # Need previous node to link its next to temp's next
            temp = temp.next
        
        # If data is not found 
        if temp is None:
            return

        # Connect the previous node with temp's next 
        prev.next = temp.next

        # Get rid of the found node 
        temp = None
    
    def deleteNodepos(self, position):

        # hold the head in a temp variable 
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        # Find the previous node 
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next # Hold the next value when the node is deleted

        temp.next = None # Delete the node

        temp.next = next # Point to the next node 
    
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

if __name__ == '__main__':
    
    llist = LinkedList()

    llist.append(1)
    llist.append(4)
    llist.append(1)
    llist.append(12)
    llist.append(1)

    llist.deleteNodepos(3)

    llist.printList()
    
