def insert_sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i-1
        while (cur < arr[j] and j>=0):
            arr[j+1] = arr[j] 
            j = j-1
        arr[j+1] = cur

arr = input("enter arr elements:")
arr = [int(x) for x in arr.split()]

insert_sort(arr)
print(f"Sorted Array is: {arr}")