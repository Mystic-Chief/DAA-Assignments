"""
10. N Meetings in one Room
"""

class Solution(object):
    def maxMeetings(self, start, end, n):
        """
        :type start: List[int]
        :type end: List[int]
        :type n: int
        :rtype: int
        """
        meetings = sorted(zip(start, end), key=lambda x: x[1])
        last_end_time = -1
        count = 0
        
        for s, e in meetings:
            if s > last_end_time:
                count += 1
                last_end_time = e
        
        return count

