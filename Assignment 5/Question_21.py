"""
21. Huffman Coding
"""

import heapq

class TreeNode(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

class Solution(object):
    def huffmanCoding(self, characters, frequencies):
        """
        :type characters: List[str]
        :type frequencies: List[int]
        :rtype: TreeNode
        """
        heap = [TreeNode(char, freq) for char, freq in zip(characters, frequencies)]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = TreeNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)
        
        return heap[0]

