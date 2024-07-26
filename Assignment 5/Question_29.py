"""
29. Disjoint Intervals
"""

class Solution(object):
    def disjointIntervals(self, intervals):
        """
        :type intervals: List[Tuple[int, int]]
        :rtype: List[Tuple[int, int]]
        """
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        result = []
        
        for interval in intervals:
            if interval[0] > end:
                result.append(interval)
                end = interval[1]
        
        return result

