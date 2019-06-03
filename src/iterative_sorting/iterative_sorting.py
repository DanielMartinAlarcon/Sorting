# Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        # swap current and smallest elements
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# implement the Bubble Sort function below
def bubble_sort( arr ):
    

    while True:
        done = True
        # Loop all the way through
        for i in range(1, len(arr)):
            # If two elements are out of order, swap them
            if arr[i] < arr[i-1]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                done = False
        # If you reach the end without swapping, finish
        if done:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # Check for negative numbers
    if not all([x > -1 for x in arr]):
        return "Error, negative numbers not allowed in Count Sort"
    
    

    return arr

arr3 = [1, 5, -2, 4, 3]
print(count_sort(arr3))