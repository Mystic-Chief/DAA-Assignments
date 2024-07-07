"""
22. Find sum of Array elements using recursion
"""

class Solution(object):
    def sumArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 0:
            return 0
        return arr[0] + self.sumArray(arr[1:])

