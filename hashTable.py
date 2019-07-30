# Hash table implementation in Python
# With linear probing, going up by 1

class HashTable:

    def __init__(self):

        # Initial size of hash table
        self.size = 11

        #This is where the keys are stored
        self.slots = [None] * self.size 

        #This is wehre the values are stored
        self.data = [None] * self.size 
    
    def put(self, key, data):
        hashValue = self.hash_function(key, len(self.slots))

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data #replace
            else:
                nextSlot = self.rehash(hashValue, len(self.slots))
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data
    
    def hash_function(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1)%size
    
    def get(self, key):
        starSlot  = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = starSlot

        while self.slots[position] != None and not found and not stop: 
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == starSlot:
                    stop = True
        
        return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == '__main__':
    H=HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"
    print(H.slots)
    print(H.data)