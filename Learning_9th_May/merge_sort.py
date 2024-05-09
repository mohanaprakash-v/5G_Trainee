def merge_sort(array):
    #split operation
    
    if len(array) > 1:
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]
        
        merge_sort(left)
        merge_sort(right)

        lp=0 #[3]
        rp=0 #[7]
        fp=0 #[ , ]

    #sort operation
        while (lp<len(left) and rp<len(right)):
            if left[lp] < right[rp]:
                array[fp] = left[lp]
                lp += 1
            else:
                array[fp] = right[lp]
                rp += 1
            fp += 1
        
        #merge operation
        while lp<len(left):
            array[fp] = left[lp]
            lp+=1
            fp+=1

        while rp<len(right):
            array[fp] = right[rp]
            rp+=1
            fp+=1

array = [3,1,4,7,6]
print(f"Before sorting: {array}")
merge_sort(array)
print(f"After sorting: {array}")