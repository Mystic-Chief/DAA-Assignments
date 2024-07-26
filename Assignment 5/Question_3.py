"""
3. Check if possible to survive on island
"""

class Solution(object):
    def canSurvive(self, S, N, M):
        """
        :type S: int
        :type N: int
        :type M: int
        :rtype: bool
        """
        if M > N:
            return False
        
        daysWithoutSunday = (S // 7) * 6 + (S % 7)
        if S * M <= daysWithoutSunday * N:
            return True
        return False

