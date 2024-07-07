"""
3. Given two numbers x and y find the product using recursion
"""

class Solution(object):
    def product(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if y == 0:
            return 0
        if y > 0:
            return x + self.product(x, y - 1)
        if y < 0:
            return -self.product(x, -y)

