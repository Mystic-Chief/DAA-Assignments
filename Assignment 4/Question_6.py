"""
6. K Weakest Rows in a Matrix
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(range(len(mat)), key=lambda x: (sum(mat[x]), x))[:k]
