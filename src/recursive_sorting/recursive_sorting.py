# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    for i in range(elements):
        if len(arrA) == 0 or len(arrB) == 0:
            merged_arr = merged_arr[:i] + arrA + arrB
            break

        if arrA[0] < arrB[0]:
            smallest = arrA.pop(0)
        else:
            smallest = arrB.pop(0)

        merged_arr[i] = smallest
    
    return merged_arr


# implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Empty or one-element arrays are already ordered
    if len(arr) <= 1:
        return arr
    else:
        i = len(arr) // 2
        return merge(merge_sort(arr[:i]), merge_sort(arr[i:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

# import random
# arr1 = random.sample(range(200), 10)
# arr2 = []
# arr3 = [2]
# arr4 = random.sample(range(200), 5)
# # arr4 = [4]


# print(merge_sort(arr2))
# print(merge_sort(arr3))
# print(merge_sort(arr1))
# assert merge(sorted(arr1), sorted(arr4)) == sorted(arr1 + arr4)

# print(merge(sorted(arr1), sorted(arr4)))
# print(sorted(arr1 + arr4))