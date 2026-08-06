class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        total = 0
        for i in range(len(nums)):
            total = total + nums[i]
            res.append(total)
        return res