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
        

    """
    class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            elif total < target:
                left += 1

            else:
                right -= 1

        """


        