"""
16. Minimum Cost to Cut Ropes
"""

import heapq

class Solution(object):
    def minCost(self, ropes):
        """
        :type ropes: List[int]
        :rtype: int
        """
        heapq.heapify(ropes)
        total_cost = 0
        
        while len(ropes) > 1:
            cost = heapq.heappop(ropes) + heapq.heappop(ropes)
            total_cost += cost
            heapq.heappush(ropes, cost)
        
        return total_cost

