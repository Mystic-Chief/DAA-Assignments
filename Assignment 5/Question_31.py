"""
31. Seats
"""

class Solution(object):
    def seats(self, A):
        """
        :type A: str
        :rtype: int
        """
        occupied = [i for i, seat in enumerate(A) if seat == 'x']
        if not occupied:
            return 0
        
        median = occupied[len(occupied) // 2]
        moves = 0
        
        for i, seat in enumerate(occupied):
            moves += abs(seat - (median - (len(occupied) // 2 - i)))
        
        return moves
