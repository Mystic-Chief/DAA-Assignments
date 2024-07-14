"""
11. Special Array with X elements Greater than or equal X
"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            if sum(num >= x for num in nums) == x:
                return x
        return -1
