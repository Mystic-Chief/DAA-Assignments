"""
25. Compute the factorial of a number using recursion
"""

class Solution(object):
    def factorial(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        return n * self.factorial(n - 1)
