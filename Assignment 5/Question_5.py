"""
5. Fractional Knapsack
"""

class Solution(object):
    def fractionalKnapsack(self, W, items):
        """
        :type W: int
        :type items: List[Tuple[int, int]] # (value, weight)
        :rtype: float
        """
        items.sort(key=lambda x: x[0] / x[1], reverse=True)
        total_value = 0.0
        
        for value, weight in items:
            if W == 0:
                break
            if weight <= W:
                total_value += value
                W -= weight
            else:
                total_value += value * (W / weight)
                W = 0
                
        return total_value

