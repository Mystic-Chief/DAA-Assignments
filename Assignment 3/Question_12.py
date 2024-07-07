"""
12. Compute sum of first N natural numbers using recursion
"""

class Solution(object):
    def sumOfNNumbers(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        return N + self.sumOfNNumbers(N - 1)

