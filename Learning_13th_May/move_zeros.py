# 283. move zeros | leet code problem

class Solution(object):
    def moveZeroes(self, nums):
        """
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[a]=nums[a],nums[i]
                a+=1
