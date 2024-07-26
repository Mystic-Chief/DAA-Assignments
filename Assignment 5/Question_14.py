"""
14. Merge Intervals
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Tuple[int, int]]
        :rtype: List[Tuple[int, int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        
        return merged

