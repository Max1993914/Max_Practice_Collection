"""
确认给定二叉树是否为合格的二叉搜索树：
1. 二叉搜索树的左子树值全部小于当前节点
2. 二叉搜索树的右子树值全部大于当前节点
3. 左右子树同样要是二叉搜索树

思路1：中序遍历
二叉搜索树的中序遍历必然是升序的，只需要判断这个就好了。
"""


def is_valid_BST(root):
    lis = []

    def recur(node):
        if not node:
            return

        recur(node.left)
        lis.append(node.val)
        recur(node.right)

    recur(root)
    for i in range(1, len(lis)):
        if lis[i] <= lis[i - 1]:
            return False
    return True
