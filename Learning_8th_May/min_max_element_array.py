from array import *
g = [2,1,3,4,7,6]
arr = array('i', g)
sort = sorted(g)
print(f"sorted array: {sort}")
print(f"min element is {min(sort)} and max element is {max(sort)}")

def min_element(arr, n):
    first = arr[0]
    for i in range(n):
        min(first,arr[i])
    return first

def max_element(arr, n):
    first = arr[0]
    for i in range(n):
        max(first,arr[i])
    return first

arr = [3,4,5]
n = len(arr)
print(min_element(arr, n))


