"""
14. Sort Array by Increasing Frequency
"""
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], x))
