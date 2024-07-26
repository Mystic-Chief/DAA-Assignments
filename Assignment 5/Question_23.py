"""
23. Policeman Catch Thieves
"""

class Solution(object):
    def catchThieves(self, arr, n, k):
        """
        :type arr: List[str]
        :type n: int
        :type k: int
        :rtype: int
        """
        thieves = []
        police = []
        
        for i in range(n):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thieves.append(i)
        
        i, j = 0, 0
        caught = 0
        
        while i < len(thieves) and j < len(police):
            if abs(thieves[i] - police[j]) <= k:
                caught += 1
                i += 1
                j += 1
            elif thieves[i] < police[j]:
                i += 1
            else:
                j += 1
        
        return caught

