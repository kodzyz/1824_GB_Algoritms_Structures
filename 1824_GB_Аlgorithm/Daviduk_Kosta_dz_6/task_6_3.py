# 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root

        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)

        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left or right:
            return left or right
