"""
7. For any positive value of N, print N to 1 without using for or while loops via recursion (Countdown)
"""

class Solution(object):
    def printNToOne(self, N):
        """
        :type N: int
        :rtype: None
        """
        if N == 0:
            return
        print(N, end=' ')
        self.printNToOne(N - 1)

