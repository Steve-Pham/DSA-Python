# Merge sort implementation in Python

# Time complexity of Merge Sort

def merge(arr, arr1, arr2):

    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i+=1 
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1
        print(arr[k])

    # Check if any values are left in the sub arrays
    while i < len(arr1): 
        arr[k] = arr1[i] 
        i+=1
        k+=1
          
    while j < len(arr2): 
        arr[k] = arr2[j] 
        j+=1
        k+=1
    


def merge_sort(arr):
    
    # Array must have a length of greater than 1

    if len(arr) > 1:

        mid = len(arr)//2

        arr1 = arr[:mid]
        arr2 = arr[mid:]

        merge_sort(arr1)
        merge_sort(arr2)
        
        merge(arr, arr1, arr2)

if __name__ == '__main__':
    
    A = [64, 25, 12, 22, 11] 
    # Driver code to test above 
    merge_sort(A)
    print ("Sorted array") 
    for i in range(len(A)): 
        print("%d" %A[i]), 