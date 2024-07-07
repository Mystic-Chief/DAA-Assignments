"""
34. Compute the GCD of two numbers using Euclidean Algorithm
"""

class Solution(object):
    def gcd(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        return self.gcd(b, a % b)

