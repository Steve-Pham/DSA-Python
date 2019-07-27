# Insertion sort implementation in Python

# Time Complexity of Insertion Sort is O(n^2)

def insertion_sort(arr):
    
    for i in range(1, len(arr)):

        current_item = arr[i]

        j = i-1

        while j>=0 and current_item < arr[j]:
            arr[j+1] = arr[j]
            j-=1 
        
        arr[j+1] = current_item

if __name__ == '__main__':
    
    arr = [12, 11, 13, 5, 6] 
    insertion_sort(arr) 
    for i in range(len(arr)): 
        print ("% d" % arr[i])