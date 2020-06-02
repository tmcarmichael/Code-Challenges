"""
226. Invert Binary Tree

Q: https://leetcode.com/problems/invert-binary-tree/
A: https://leetcode.com/problems/invert-binary-tree/discuss/665457/recursive-python3-and-js-solutions
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
