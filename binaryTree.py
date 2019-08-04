class BinarySearchTree:
    
    # Initialize the Binary Tree
    def __init__(self):
        self.root = None
        self.size = 0 

    # Size of the Binary Tree 
    def length(self):
        return self.size
    
    # Private operator of the obtaining the size of the Binary Tree
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    # Inserting a node into a tree
    def put(self, key, val):
        # If there is an existing root already, call helper put helper function
        if self.root:
            self._put(key, val, self.root)
        # If there is no root, then make a root node
        else:
            self.root = TreeNode(key, val)
        self.size += 1 # Increase the size of the tree by 1
    

    def _put(self, key ,val, currentNode):
        # If the key is in left sub tree
        if key < currentNode.key:
            # If the node has a left child
            if currentNode.hasLeftChild():
                # Recursive call on put function, but use currentNode as the currentNode's left child
                self._put(key, val, currentNode.leftChild)
            else:
                # If the current node's left child is empty, place a new node there
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        # If the key is in right sub tree
        else:
            # if the node has a right child already
            if currentNode.hasRightChild():
                #Recursive call on put function but use curerntNode as the currentNode's right child
                self._put(key, val, currentNode.rightChild)
            else:
                # If the current node has no right child, then put the new node there
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    # Overload the [] operator for assignment 
    # example: H[3] = 'cat'
    def __setitem__(self,k,v):
        self.put(k,v)
    
    # Get method to retrieve a node from the tree
    def get(self, key):
        # If a root exists
        if self.root:
            # Get node from helper get function
            res = self._get(key, self.root)
            # If a node was found, return the data
            if res:
                return res.payload
            # If a node was not found
            else:
                return None
        else:
            return None
    
    # Get helper function
    def _get(self, key, currentNode):
        # If node doesn't exist, return None
        if not currentNode:
            return None
        # If the node was found, perfect matching keys
        elif currentNode.key == key:
            return currentNode
        # If the key is less than the currentNode, then search the left sub tree, recursive call
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        # If the key is greater than the currentNode, then search the right sub tree, recursive call
        else:
            return self._get(key, currentNode.rightChild)

    # This method makes it look like we are using a dictionary
    def __getitem__(self, key):
        return self.get(key)
    
    # __contains__ overloads the "in" operator
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
    
    # Delete a node function
    def delete(self, key):
        # If there exists a tree
        if self.size > 1:
            # Get the node 
            nodeToRemove = self._get(key, self.root)
            # If there exists a node with the key, remove it 
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size += 1
            # If such node doesn't exists
            else:
                raise KeyError('Error, key not in tree')
        # If the tree only has a root, and no other nodes
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        # If there is no tree, then throw an error
        else:
            raise KeyError('Error, key not in tree')
    
    # Override some function 
    def __delitem__(self, key):
        self.delete(key)

    # Remove function
    def remove(self, currentNode):
        # If the current node is a leaf
        if currentNode.isLeaf():
            # If the currentNode is a left node, get rid of the left child in the parent node
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            # If the current node is a right node, get rid of the right child in the parent node
            else:
                currentNode.parent.rightChild = None
        # If the currentNode has two children
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        # If the currentNode has one child 
        else:
            # If the node has a left child 
            if currentNode.hasLeftChild():
                # If the current node is a left child
                if currentNode.isLeftChild():
                    # Make currentNode's left child parent, the parent of currentNode's
                    currentNode.leftChild.parent = currentNode.parent
                    # Make the currentNode's parent leftchild, the currentNode's left child,
                    currentNode.parent.leftChild = currentNode.leftChild
                # If the current node is a right child 
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                # If current node is a root 
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            # If current node has right child 
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeDatac(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


class TreeNode:
    
    # Constructor, with key, payload with the data, left child, right child
    def __init__(self, key, val, left=None, right=None, parent=None):
        
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild= right
        self.parent = parent
    
    # If node has left child
    def hasLeftChild(self):
        return self.leftChild
    
    # If node has right child
    def hasRightChild(self):
        return self.rightChild

    # This returns true if the node is a left child
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    # This returns true if the node is a right child 
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    # If the node is current a root
    # This node will have no parent 
    def isRoot(self):
        return not self.parent
    
    # If the node is a leaf, so it will not have any child nodes
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    
    # If the node has a left child or a right child
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    
    # If the node has a left child and right child 
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    
    # Change node data 
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    # TreeNode class 
    def findSuccessor(self):
        succ = None
        # If currentNode has a right child, then the successor is the smallest key
        # in the right sub tree
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                # If the node has no right child and is the left of its parent
                # Then the parent is the successor
                if self.isLeftChild():
                    succ = self.parent
                # If the node is the right child of its parent, and itself has no right child
                # Then the successor to this node is the successor of its parent, excluding this node
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    
    # Continuously look in the left sub tree to find the smallest key
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent 
    
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

if __name__ == '__main__':
    
    mytree = BinarySearchTree()
    mytree[2] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[1] = "at"
    mytree[3] = 'aye'

    print(mytree[6])
    print(mytree[2])

