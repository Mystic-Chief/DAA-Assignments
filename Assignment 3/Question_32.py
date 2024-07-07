"""
32. Print all leaf nodes of a Binary Search Tree using recursion
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def printLeafNodes(self, root):
        """
        :type root: TreeNode
        :rtype: None
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            print(root.val, end=" ")
            return
        if root.left:
            self.printLeafNodes(root.left)
        if root.right:
            self.printLeafNodes(root.right)


