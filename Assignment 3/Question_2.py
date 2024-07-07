"""
2. Compute the product of digits of a number using recursion
"""

class Solution(object):
    def productOfDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n % 10 == n:
            return n
        return (n % 10) * self.productOfDigits(n // 10)


