"""
1. Compute the sum of digits of a number using recursion
"""

class Solution(object):
    def sumOfDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        return n % 10 + self.sumOfDigits(n // 10)


