class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        if len(nums) < 1:
            return 0
        nums.sort()
        for i in range(len(nums)-1):
            gap = nums[i+1] - nums[i]
            if gap > res:
                res = gap
        return res

            

        