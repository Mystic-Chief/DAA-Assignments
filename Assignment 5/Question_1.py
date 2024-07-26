"""
1. Select k elements from the array such that their sum is maximized
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


