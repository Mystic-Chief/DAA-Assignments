"""
7. Chocolate Distribution
"""

class Solution(object):
    def chocolateDistribution(self, chocolates, students):
        """
        :type chocolates: List[int]
        :type students: int
        :rtype: int
        """
        if students == 0 or len(chocolates) == 0:
            return 0
        if len(chocolates) < students:
            return -1
        
        chocolates.sort()
        min_diff = float('inf')
        
        for i in range(len(chocolates) - students + 1):
            min_diff = min(min_diff, chocolates[i + students - 1] - chocolates[i])
        
        return min_diff

