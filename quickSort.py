# Quick sort implementation in Python

# Worst case: O(n^2)
# Average case: O(nlogn)

def partition(arr, low, high):

    pivot = arr[high]
    i = low-1

    for j in range(low, high):

        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]

    # Return pivot 
    return i+1

def quick_sort(arr, low, high):
    
    if low < high:

        #Get pivot
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)



if __name__ == '__main__':
    
    arr = [10, 7, 8, 9, 1, 5]  
    quick_sort(arr,0, len(arr)-1) 
    for i in range(len(arr)-1): 
        print(arr[i])