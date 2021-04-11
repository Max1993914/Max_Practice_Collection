"""
给定一个二叉树，判断它是否是镜像对称的，例如：
        1
    2        2
3     4    4     3

思路1：递归
递归条件，对于每一个点：
1. 如果只有左子节点，没有右子节点，或者只有右子节点，没有左子节点，那么都是False
2. 如果左右子节点都没有，则返回True
3. 如果左节点值=右节点值，递归继续判断：recur(left.left, right.right), recur(left.right, right.left)
时间复杂度：因为遍历了这棵树，时间复杂度为O(n)
空间复杂度：调用栈取决于树的深度，这里深度最大不超过n，时间复杂度O(n)

思路2：迭代：
在队列中同时取出两个节点left, right，判断这两个节点的值是否相等，
然后把他们的孩子中按照(left.left, right.right) 一组，(left.right, right.left)一组放入队列中。
时间复杂度：因为遍历了这棵树，为O(n)
空间复杂度：O(n)
"""


# 递归
def is_symmetric1(root):
    if not root:
        return True

    def recur(left, right):
        if not left and not right:
            return True
        if left and not right:
            return False
        if right and not left:
            return False

        return left.val == right.val and recur(left.left, right.right) and recur(left.right, right.left)

    return recur(root.left, root.right)


# 迭代
def is_symmetric2(root):
    if not root:
        return True

    queue = list()
    queue.append((root.left, root.right))
    while queue:
        left, right = queue.pop(0)
        if not left and not right:
            continue
        if not left and right:
            return False
        if not right and left:
            return False
        if left.val != right.val:
            return False
        queue.append((left.left, right.right))
        queue.append((right.left, left.right))
    return True
