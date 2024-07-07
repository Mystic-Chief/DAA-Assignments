"""
4. Find the value of 'a' raised to the power 'b' using recursion
"""

class Solution(object):
    def power(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return 1
        return a * self.power(a, b - 1)

