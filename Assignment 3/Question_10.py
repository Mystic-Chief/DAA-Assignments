"""
10. Reverse a string using recursion
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        return self.reverseString(s[1:]) + s[0]

