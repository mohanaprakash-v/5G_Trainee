# 217. Contain Duplicates | leetcode problem

def duplicate(nums):
    s=set()
    for i in nums:
        if i in s:
            return True #duplicate
        else:
            s.add(i)
    return False #no duplicate

nums = [1,2,3]
nums1 = [1,1,1,2,2,3]
print(duplicate(nums))
print(duplicate(nums1))