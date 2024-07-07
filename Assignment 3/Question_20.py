"""
20. Count Number of Zeros in a Number using recursion
"""

class Solution(object):
    def countZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n < 10:
            return 0
        return (1 if n % 10 == 0 else 0) + self.countZeros(n // 10)

