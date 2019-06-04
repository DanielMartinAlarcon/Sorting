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
def count_sort( arr):
    import numpy as np
    # Check for negative numbers
    if not all([x > -1 for x in arr]):
        return "Error, negative numbers not allowed in Count Sort"
    
    # Check for empty inputs
    if arr == []:
        return arr

    # Make a count vector that can count all numbers up to the max
    counts = np.zeros(max(arr)+1, dtype=int)
    
    # Loop through the array, using its integer value as the
    # index in the count array, and increasing that count by 1
    for x in arr:
        counts[x] += 1
    # print(f'counts: {counts}')

    # Create next_index, a cumulative version of counts
    next_index = counts.copy()
    for i in range(1, len(next_index)):
        next_index[i] = next_index[i-1] + counts[i-1]
    # print(f'next_index: {next_index}')

    
    # Create a new array of just zeros, same length as the original
    arr2 = [0]*len(arr)

    # Loop over the original list, placing each item at the position
    # indicated by counts and adding one to count at the position where
    # an item was added.
    for x in arr:
        try:
            arr2[next_index[x]] = x
            next_index[x] += 1
        except:
            print(f'x: {x}')
            print(f'arr2: {arr2}')
            print(f'next_index: {next_index}')
            print(f'next_index[x]: {next_index[x]}')
            # print(f'next_index update: {next_index}')
            print()
        # break
    return arr2

import random
arr = random.sample(range(200), 50)
print(count_sort(arr))
print(sorted(arr))
print(arr)
