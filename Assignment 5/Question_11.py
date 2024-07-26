"""
11. Find Maximum Meetings in One Room
"""

class Solution(object):
    def maxMeetings(self, start, end, n):
        """
        :type start: List[int]
        :type end: List[int]
        :type n: int
        :rtype: List[int]
        """
        meetings = sorted(enumerate(zip(start, end)), key=lambda x: x[1][1])
        last_end_time = -1
        selected_meetings = []
        
        for index, (s, e) in meetings:
            if s > last_end_time:
                selected_meetings.append(index + 1)
                last_end_time = e
        
        return selected_meetings

