"""
30. Largest Permutation
"""

class Solution(object):
    def largestPermutation(self, k, arr):
        """
        :type k: int
        :type arr: List[int]
        :rtype: List[int]
        """
        pos = {v: i for i, v in enumerate(arr)}
        
        for i in range(len(arr)):
            if k == 0:
                break
            if arr[i] != len(arr) - i:
                temp = pos[len(arr) - i]
                pos[arr[i]] = pos[len(arr) - i]
                pos[len(arr) - i] = i
                arr[i], arr[temp] = arr[temp], arr[i]
                k -= 1
        
        return arr

