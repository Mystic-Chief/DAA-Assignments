"""
8. Shop in a Candy Store
"""

class Solution(object):
    def candyStore(self, candies, N, K):
        """
        :type candies: List[int]
        :type N: int
        :type K: int
        :rtype: Tuple[int, int]
        """
        candies.sort()
        
        min_cost, max_cost = 0, 0
        i, j = 0, N - 1
        
        while i <= j:
            min_cost += candies[i]
            j -= K
            i += 1
        
        i, j = 0, N - 1
        
        while i <= j:
            max_cost += candies[j]
            j -= 1
            i += K
        
        return min_cost, max_cost
