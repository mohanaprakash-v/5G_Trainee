# class Solution(object):
#     def productExceptSelf(self, nums):
#         prefix = 1
#         suffix = 1
#         final = [1]*len(nums)
#         for i in range(len(nums)):
#             final[i] = prefix
#             prefix = prefix * nums[i]
#         for i in range(len(nums)-1,-1,-1):
#             final[i] = final[i]*suffix
#             suffix = suffix * nums[i]
#         return final

import copy
nums = [1,2,3,4]
final = copy.deepcopy(nums)

for i in range(len(nums)):
    index = i
    sorted = copy.deepcopy(nums)
    sorted.pop(i)
    count = 1

    for j in sorted:
        count = count*j
    final[i] = count
print(final)