# 118. pascal's triangle | leetcode problem

class Solution(object):
    def generate(self, numRows):
        result =[[1]]
        for i in range(numRows-1):
            temp = [0]+result[i]+[0]
            result_temp=[]
            for i in range(len(temp)-1):
                result_temp.append(temp[i]+temp[i+1])
            result.append(result_temp)
        return result