"""
226. Invert Binary Tree

Q: https://leetcode.com/problems/invert-binary-tree/
A: 
"""


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return

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
