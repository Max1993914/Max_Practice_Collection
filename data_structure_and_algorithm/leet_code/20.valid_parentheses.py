"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
例如：{}(), {()}

思路：
首先先排除一个错误思路：是不是两边的括号种类数量相等就行了呢？并不是，例如{[}]这种就不可以。
除了两边括号种类数量相等之外，最新的左括号需要最先闭合，这就非常符合栈后进先出的特性
"""


def is_valid(s):
    if len(s) % 2 == 1:  # 节省时间，因为奇数个字符势必不能闭合。
        return False

    stack = list()
    pair = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for char in s:
        if char in pair:
            stack.append(char)
        else:
            if stack and pair[stack[-1]] == char:
                stack.pop()
            else:
                return False

    if stack:
        return False
    return True


a = "{}()[]"
assert is_valid(a)
b = "{[]}"
assert is_valid(b)
c = "{(})"
assert not is_valid(c)
