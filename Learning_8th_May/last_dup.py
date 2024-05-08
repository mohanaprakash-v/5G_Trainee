def duplicate(arr, n):
    if arr == None or n <= 0:
        return

    for i in range(n-1, 0, -1):
        if arr[i-1]==arr[i]:
            print(f"Last duplicate element is: {arr[i]}")
            return
    print("No duplicate")

arr = [11, 2, 3, 5, 5, 6]
n = len(arr)
duplicate(arr,n)
