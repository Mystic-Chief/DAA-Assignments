"""
4. Shortest Job First
"""

class Solution(object):
    def shortestJobFirst(self, jobs):
        """
        :type jobs: List[int]
        :rtype: int
        """
        jobs.sort()
        total_waiting_time, current_time = 0, 0
        for job in jobs:
            total_waiting_time += current_time
            current_time += job
        return total_waiting_time

