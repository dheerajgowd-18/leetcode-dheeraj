class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            res.append(nums[i]**2)
        res.sort()
        return res
            
        
            


        