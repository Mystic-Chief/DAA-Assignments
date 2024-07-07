"""
13. Pow(x, n)
"""

class Solution(object):
    def pow(self, x, n):
        """
        :type x: int
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        return x * self.pow(x, n - 1)
