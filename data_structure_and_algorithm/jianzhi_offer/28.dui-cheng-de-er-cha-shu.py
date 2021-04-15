"""
判断二叉树是否为对称二叉树

思路：递归
"""


def is_symmetric(root):
    if not root:
        return True

    def recur(left, right):
        if not left and not right:
            return True
        if (left and not right) or (right and not left):
            return False

        # 一个树是否为对称需要判断：1. 左右子树两值相等，并且左.左 = 右.右 然后左.右 = 右.左
        if left.val == right.val and recur(left.left, right.right) and recur(left.right, right.left):
            return True
        else:
            return False

    return recur(root.left, root.right)