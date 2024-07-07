"""
11. Check if a String is Palindrome using recursion
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return self.isPalindrome(s[1:-1])


