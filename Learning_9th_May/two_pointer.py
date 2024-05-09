def two_point(arr):
    n=len(arr)
    lp = 0
    h=1
    rp = n-1
    t_sum = 17
    while lp<rp:
        fp = arr[lp] + arr[rp]
        if fp == t_sum:
            print(f"Target achieved by adding index: {lp} and {rp}")
            h=0
            break
        elif fp  < t_sum:
            lp+=1
        elif fp > t_sum:
            rp-=1
    if h == 1:
        print("No combinations")
        
arr = [1,2,3,4,5,6,7]
two_point(arr)
