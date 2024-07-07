"""
26. Sum Triangle
"""

class Solution(object):
    def sumTriangle(self, arr):
        """
        :type arr: List[int]
        :rtype: None
        """
        if len(arr) == 0:
            return
        if len(arr) == 1:
            print(arr[0])
            return
        
        new_arr = [arr[i] + arr[i+1] for i in range(len(arr)-1)]
        self.sumTriangle(new_arr)
        print(arr)

