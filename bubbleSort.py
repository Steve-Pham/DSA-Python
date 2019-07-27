# Bubble sort implementation in Python 

# Time Complexity of Bubble Sort: O(n^2)

def bubble_sort(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':

    arr = [64, 34, 25, 12, 22, 11, 90] 
  
    bubble_sort(arr) 
    for i in range(len(arr)): 
        print(arr[i])