# Search algorithm implementations in Python

# Linear Search Algorithm, Time Complexity: O(n)
def linear_search(arr, item):
    
    # Search every element in the array
    for num in arr:
        print(num)
        if (num == item):
            return True

    return False

# Binary search Algorithm using recursion, Time Complexity: O(logn)
def binary_search(arr, low, high, item):

    if high >= low: 

        # Calculate the middle
        mid = (low + high) / 2 

        # If value is found in the middle of the list, return true
        if (arr[mid] == item):
            return True
        elif (arr[mid] > item):
            return binary_search(arr, low, mid-1, item)
        else:
            return binary_search(arr, mid+1, high, item)
    
    else: 
        return False

arr = [2, 3, 4, 10, 40 ]
result = binary_search(arr, 0, len(arr)-1, 10)

if result:
    print('Success')
else:
    print('Failed')

'''
if (linear_search(arr, 40)):
    print('Search Successful!')
else:
    print('Not successful!')
'''

