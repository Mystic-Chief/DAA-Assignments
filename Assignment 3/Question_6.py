"""
6. For any positive value of N, print 1 to N without using for or while loops via recursion (Reverse Countdown)
"""

class Solution(object):
    def printOneToN(self, N):
        """
        :type N: int
        :rtype: None
        """
        if N == 0:
            return
        self.printOneToN(N - 1)
        print(N, end=' ')

