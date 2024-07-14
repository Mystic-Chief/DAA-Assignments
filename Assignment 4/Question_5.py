"""
5. Sort Even and Odd Indices Independently
"""
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted(nums[i] for i in range(0, len(nums), 2))
        odds = sorted(nums[i] for i in range(1, len(nums), 2))
        return [evens[i // 2] if i % 2 == 0 else odds[i // 2] for i in range(len(nums))]
