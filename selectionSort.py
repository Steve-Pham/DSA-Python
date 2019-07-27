# Selection sort implementation in Python

# Time Complexity of this sorting algorithm: O(n^2)

def selection_sort(arr):
    
    for i in range(len(arr)):

        min_index = i

        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    
    A = [64, 25, 12, 22, 11] 
    # Driver code to test above 
    selection_sort(A)
    print ("Sorted array") 
    for i in range(len(A)): 
        print("%d" %A[i]),  