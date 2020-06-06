"""
226. Invert Binary Tree

Q: https://leetcode.com/problems/invert-binary-tree/
A: https://leetcode.com/problems/invert-binary-tree/discuss/665457/recursive-python3-and-js-solutions
"""
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root

        def recur(root):
            if root.left == None and root.right == None:
                return
            root.left, root.right = root.right, root.left
            if root.right:
                recur(root.right)
            if root.left:
                recur(root.left)
        recur(root)
        return root
