"""
15. Job Sequencing Problem
"""

class Solution(object):
    def jobScheduling(self, jobs, n):
        """
        :type jobs: List[Tuple[int, int, int]] # (job id, deadline, profit)
        :type n: int
        :rtype: int
        """
        jobs.sort(key=lambda x: x[2], reverse=True)
        slots = [-1] * n
        max_profit = 0
        
        for job in jobs:
            job_id, deadline, profit = job
            for j in range(min(n, deadline) - 1, -1, -1):
                if slots[j] == -1:
                    slots[j] = job_id
                    max_profit += profit
                    break
        
        return max_profit

