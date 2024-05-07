arr = input("Enter the elements:")
arr = [int(x) for x in arr.split()]

for i in range(len(arr)-1):
    min = i #index arr[i]
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min]:
            min = j
    arr[min], arr[i] = arr[i], arr[min]
print(f"Sorted array is: {arr}")
