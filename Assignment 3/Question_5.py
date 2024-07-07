"""
5. Convert decimal to binary using recursion
"""

class Solution(object):
    def decimalToBinary(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "0"
        if n == 1:
            return "1"
        return self.decimalToBinary(n // 2) + str(n % 2)


