"""
24. Find maximum and minimum of Array elements using recursion
"""

class Solution(object):
    def findMaxMin(self, arr, n, max_val=float('-inf'), min_val=float('inf')):
        """
        :type arr: List[int]
        :type n: int
        :rtype: Tuple[int, int]
        """
        if n == 0:
            return max_val, min_val
        max_val = max(max_val, arr[n-1])
        min_val = min(min_val, arr[n-1])
        return self.findMaxMin(arr, n-1, max_val, min_val)
