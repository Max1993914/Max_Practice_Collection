"""
二叉树层序遍历
"""


def level_order(root):
    if not root:
        return []

    all_results = [[root.val]]
    result = [root]
    while result:
        temp = []
        for item in result:
            if item.left:
                temp.append(item.left)
            if item.right:
                temp.append(item.right)
        result = temp
        if result:
            all_results.append([item.val for item in result])
    return all_results
