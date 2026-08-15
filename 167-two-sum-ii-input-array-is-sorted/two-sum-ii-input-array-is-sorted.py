class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,num in enumerate(numbers,1):
            complement = target - num
            if complement in d:
                return [d[complement],i]
            d[num] = i
        


        