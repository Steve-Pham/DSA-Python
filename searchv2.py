# BFS and DFS implementation in Python

class Node:

    def __init__(self, id):
        self.id = id 
        self.adjacent = []
    
class Graph:

    def __init__(self):
        self.nodeLookup = {}
    
    def getNode(self, id):
        return self.nodeLookup[id]
    
    def addEdge(self, source, destination):
        pass
    
    def hasPathDFS(self, source, destination):
        s = self.getNode(source)
        d = self.getNode(destination)
        visited = {} #Set
        return self.PathDFS(s, d, visited)
    
    def PathDFS(self, source, destination, visited):

        if source.id in visited:
            return False
        visited.add(source.id)

        if (source == destination):
            return True

        for child in source.adjacent:
            if (self.PathDFS(child, destination, visited)):
                return True
        
        return False
    
    def hasPathBFS(self, source, destination):
        nextTovisit = []
        visited = set()
        nextTovisit.append(source)
        while not len(nextTovisit) == 0:
            node = nextTovisit.pop()
            if (node == destination):
                return True
        
            if node.id in visited:
                continue
            
            visited.add(node.id)

            for child in node.adjacent:
                nextTovisit.append(child)
        
        return False

if __name__ == "__main__":
    pass
        
