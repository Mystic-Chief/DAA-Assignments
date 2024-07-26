"""
24. K Items with the Maximum Sum
"""

class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return sum(nums[:k])

