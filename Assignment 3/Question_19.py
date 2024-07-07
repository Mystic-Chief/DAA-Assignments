"""
19. Special Fibonacci
"""

class Solution(object):
    def specialFibonacci(self, a, b, n):
        """
        :type a: int
        :type b: int
        :type n: int
        :rtype: int
        """
        if n == 1:
            return a
        if n == 2:
            return b
        return self.specialFibonacci(a, b, n - 1) ^ self.specialFibonacci(a, b, n - 2)

