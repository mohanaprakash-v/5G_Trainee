def sel_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = input("enter arr elements:")
arr = [int(y) for y in arr.split()]
sel_sort(arr)
print(f"Sorted Array is: {arr}")