"""
22. Assign Mice to Holes
"""

class Solution(object):
    def assignMiceToHoles(self, mice, holes):
        """
        :type mice: List[int]
        :type holes: List[int]
        :rtype: int
        """
        mice.sort()
        holes.sort()
        max_time = 0
        
        for i in range(len(mice)):
            max_time = max(max_time, abs(mice[i] - holes[i]))
        
        return max_time

