"""
8. Reverse a number using recursion
"""

class Solution(object):
    def reverseNumber(self, n, rev=0):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return rev
        rev = rev * 10 + n % 10
        return self.reverseNumber(n // 10, rev)

