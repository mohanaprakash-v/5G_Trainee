# 1299. Replace elements with greatest element at rightside | leet code problem

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rightmax = -1
        for i in range(len(arr)-1,-1,-1):
            tempmax = max(rightmax,arr[i])
            arr[i] = rightmax
            rightmax = tempmax
        return arr