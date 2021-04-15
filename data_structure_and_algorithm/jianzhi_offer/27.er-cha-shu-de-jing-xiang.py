"""
输出二叉树的镜像

     3
    / \
   1   2
  / \  / \
 4   6 7  8

     3
    /  \
   2   1
 /  \  / \
8   7  6  4


思路：递归交换左右子树的指针即可
"""


def mirror_tree(root):

    def recur(root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        if root.left:
            recur(root.left)
        if root.right:
            recur(root.right)

    recur(root)
    return root

