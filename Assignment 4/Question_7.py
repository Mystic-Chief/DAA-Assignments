"""
7. Squares of a Sorted Array
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x * x for x in nums)
