"""
13. How many numbers are smaller than the current
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(num < x for num in nums) for x in nums]
