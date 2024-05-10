def calculate_subsets(res, arr, index, subset):
    res.append(subset[:])

    for i in range(index, len(arr)):
        subset.append(arr[i])
        calculate_subsets(res, arr, i+1, subset)
        subset.pop()    #backtracking applied 

def subsets(arr):
    res = []
    subset = []
    index = 0
    calculate_subsets(res, arr, index, subset)
    return res

if __name__ == "__main__":
    arr = [1,2,3]
    res = subsets(arr)

    for subset in res:
        print(*subset)