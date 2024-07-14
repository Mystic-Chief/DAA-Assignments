"""
12. Buy Two Chocolates
"""
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if len(prices) < 2 or prices[0] + prices[1] > money:
            return money
        return money - prices[0] - prices[1]
