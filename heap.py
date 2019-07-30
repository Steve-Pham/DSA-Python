# Heap Implementation in Python

# This implementation starts at index 1

class Heap: 
    
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0
    
    def perc_up(self, i):

        while i//2 > 0:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
        i = i//2

    def insert(self, item):
        self.heap.append(item)
        self.currentSize += 1
        self.perc_up(self.currentSize)

    def minChild(self, i):
        if (i*2) + 1 > self.currentSize:
            return i*2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i*2
            else:
                return i*2+1
    
    def perc_down(self, i):
        while (i*2) < self.currentSize:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc
    
    def del_min(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heap.pop()
        self.perc_down(1)
        return retval
    
    def build_heap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1
    
if __name__ == '__main__':
    alist = [9, 6, 5, 2, 3]

    myHeap = Heap()

    myHeap.build_heap(alist)

