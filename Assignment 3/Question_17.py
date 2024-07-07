"""
17. Find the nth number in a Fibonacci Series using Recursion
"""

class Solution(object):
    def fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

