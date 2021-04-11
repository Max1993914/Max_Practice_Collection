"""
二叉树的中序遍历
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    result = []
    if not root:
        return result

    def recur(node):
        if not node:
            return

        recur(node.left)
        result.append(node.val)
        recur(node.right)

    recur(root)
    return result