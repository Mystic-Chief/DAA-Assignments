"""
12. Non Overlapping Intervals
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Tuple[int, int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        count = 0
        
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
            else:
                count += 1
        
        return count

