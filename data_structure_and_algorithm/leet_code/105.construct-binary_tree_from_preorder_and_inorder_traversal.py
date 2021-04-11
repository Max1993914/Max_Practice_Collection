"""
通过前序和中序遍历构造二叉搜索树

思路：
前序遍历：根左右
中序遍历：左根右
1. 先取前序遍历第一个节点为根节点
2. 确认根节点在中序遍历的位置mid，划分为左右子树。左子树元素数量即为mid。
3. 根据重新划分的位置递归执行构造函数
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return

    root = TreeNode(val=preorder[0])
    mid = inorder.index(preorder[0])

    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])
    return root
