"""
29. Perform Insertion Sort using Recursion
"""

class Solution(object):
    def insertionSort(self, arr, n=None):
        """
        :type arr: List[int]
        :type n: int
        :rtype: List[int]
        """
        if n is None:
            n = len(arr)
        if n <= 1:
            return arr
        
        self.insertionSort(arr, n - 1)
        last = arr[n - 1]
        j = n - 2
        
        while j >= 0 and arr[j] > last:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = last
        return arr


