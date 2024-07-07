"""
27. Perform binary search using recursion
"""

class Solution(object):
    def binarySearch(self, arr, left, right, x):
        """
        :type arr: List[int]
        :type left: int
        :type right: int
        :type x: int
        :rtype: int
        """
        if right >= left:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binarySearch(arr, left, mid - 1, x)
            else:
                return self.binarySearch(arr, mid + 1, right, x)
        else:
            return -1

