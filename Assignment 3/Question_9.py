"""
9. Find length of string using recursion
"""

class Solution(object):
    def stringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        return 1 + self.stringLength(s[1:])


