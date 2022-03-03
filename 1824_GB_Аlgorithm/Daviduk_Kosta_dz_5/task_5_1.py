# 145. Binary Tree Postorder Traversal

# Given the root of a binary tree,
# return the postorder traversal of its nodes' values

# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.val)
    return 0


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

post_order(tree)

