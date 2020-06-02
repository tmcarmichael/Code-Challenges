class Solution:
    def insertIntoBST(self, root, val):
        # Recursively
        # if val < root.val:
        #     if root.left:
        #         self.insertIntoBST(root.left, val)
        #     else:
        #         root.left = TreeNode(val)
        # else:
        #     if root.right:
        #         self.insertIntoBST(root.right, val)
        #     else:
        #         root.right = TreeNode(val)
        # return root
        
        # Faster Iterative
        x=root
        while (x.left and val < x.val) or (x.right and val > x.val):
            x=x.left if val < x.val else x.right
        if val < x.val: x.left = TreeNode(val)
        else: x.right = TreeNode(val)
        return root
        
        
