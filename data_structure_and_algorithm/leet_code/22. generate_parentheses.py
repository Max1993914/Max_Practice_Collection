"""
数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。
例如输入：n = 2
输出：["(())", "()()"]
思路：
回溯法，深度优先。由于字符串是从左到右生成，所以有如下限制：
1. 左括号的数量<=n
2. 右括号的数量<=左括号数量
                                ""
                        /                \
                   左:"("               （剪）右:")"
               /             \
          左:"(("              右:"()"
          /     \              /     \
    (剪)左:"((("  右"(()"  左："()("   (剪)右:"())"
                   \              \
                    右"(())"         右"()()"
二叉树的深度是2n，
时间复杂度：
空间复杂度：
"""


def generate_parenthesis(n):
    length = n * 2
    all_results = []
    result = ""
    left = 0
    right = 0

    def back_trace(index):
        nonlocal left
        nonlocal right
        nonlocal result
        if left > n or right > left:
            return
        if index >= length:
            all_results.append(result)
            return

        result += "("
        left += 1
        back_trace(index + 1)
        result = result[:-1]
        left -= 1
        result += ")"
        right += 1
        back_trace(index + 1)
        result = result[:-1]
        right -= 1

    back_trace(0)

    return all_results
