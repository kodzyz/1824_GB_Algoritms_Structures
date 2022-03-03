# Проверить дерево на симметричность:
# 101. Symmetric Tree

# Given the root of a binary tree,
# check whether it is a mirror of itself
# (i.e., symmetric around its center)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_mirror(root):
    return check_halves(root.left, root.right)

def check_halves(left, right):
    if not left and not right:
        return True
    if left and right:
        if left.val == right.val:
            left_half = check_halves(left.left, right.right)
            right_half = check_halves(left.right, right.left)
            return left_half and right_half
    return False

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.right.right = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)

print(is_mirror(tree))

