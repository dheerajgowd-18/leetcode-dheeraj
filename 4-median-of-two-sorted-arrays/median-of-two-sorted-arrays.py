class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = 0
        num = sorted(nums1 + nums2)
        n = len(num)
        if n % 2==1:
            return float(num[n//2])
        else:
            return (num[(n//2)-1] + num[n//2])/2.0

        