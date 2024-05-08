import random

def quick_sort(arr):

    if len(arr)<=1:
        return arr
    
    pivot = random.choice(arr)

    left = []
    for i in arr:
        if i < pivot:
            left.append(i)
    
    right = []
    for i in arr:
        if i > pivot:
            right.append(i)

    mid = []
    for i in arr:
        if i == pivot:
            mid.append(i)
    
    return quick_sort(left) + mid + quick_sort(right)

arr = [3, 4, 6, 5, 1, 8, 2]
print(f"Before sorting: {arr}")
print(f"Sorted array using quick sort: {quick_sort(arr)}")


