"""
23. Find mean of Array elements using recursion
"""

class Solution(object):
    def meanArray(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        def sumArray(arr):
            if len(arr) == 0:
                return 0
            return arr[0] + sumArray(arr[1:])
        
        if len(arr) == 0:
            return 0
        total_sum = sumArray(arr)
        return total_sum / len(arr)


