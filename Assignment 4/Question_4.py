"""
4. Average Salary Excluding the Minimum and Maximum
"""
class Solution:
    def average(self, salary: List[float]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
