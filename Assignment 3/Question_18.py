"""
18. Geekonacci Number
"""

class Solution(object):
    def geekonacci(self, a, b, c, n):
        """
        :type a: int
        :type b: int
        :type c: int
        :type n: int
        :rtype: int
        """
        if n == 1:
            return a
        if n == 2:
            return b
        if n == 3:
            return c
        return self.geekonacci(a, b, c, n - 1) + self.geekonacci(a, b, c, n - 2) + self.geekonacci(a, b, c, n - 3)

solution = Solution()
print(solution.geekonacci(1, 3, 2, 4))
