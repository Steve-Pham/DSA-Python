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
        # Calculate hash value
        hashValue = self.hash_function(key, len(self.slots))

        # If slot is not taken already, insert into the hash tbale
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        # If the slot is taken already from the hash value    
        else:
            # If the key already exists, then we want to replace the data
            if self.slots[hashValue] == key:
                self.data[hashValue] = data #replace
            # If the key doesn't exist, but a different key has the same hashValue
            else:
                #Recalculate hash value
                nextSlot = self.rehash(hashValue, len(self.slots))
                # Recalculate hash until an empty slot is open using linear probing
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                #If the slot is empty, then fill slot with key and data with data
                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                #If the key was found during rehash, then replace the value 
                else:
                    self.data[nextSlot] = data
    
    def hash_function(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1)%size
    
    def get(self, key):
        startSlot  = self.hash_function(key, len(self.slots)) #suppose to be startSlot

        data = None
        stop = False
        found = False
        position = startSlot

        while self.slots[position] != None and not found and not stop: 
            # If hash was found, then get the data 
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # If hash was not found initially. then rehash until it is found
                position = self.rehash(position, len(self.slots))
                # If key was not found, basically if the hash table is looped around
                if position == startSlot:
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