"""
二叉树的最大层数

思路1：递归
deepth = max(l,r)+1
"""


def maxDepth(root):
    def recur(node):
        if not node:
            return 0
        left_height = recur(node.left)
        right_height = recur(node.right)
        return max(left_height, right_height) + 1

    return recur(root)