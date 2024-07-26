"""
13. Insert Interval
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Tuple[int, int]]
        :type newInterval: Tuple[int, int]
        :rtype: List[Tuple[int, int]]
        """
        result = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = (min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]))
            i += 1
        
        result.append(newInterval)
        
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result

