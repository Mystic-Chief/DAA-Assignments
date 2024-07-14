"""
3. Minimum Number Game
"""
class Solution:
    def minimumNumberGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums.sort()
            first_min = nums.pop(0)
            second_min = nums.pop(0)
            nums.append(first_min + second_min)
        return nums[0]
