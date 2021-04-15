"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，
但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

思路：创建一个stack，模拟压入弹出的过程
"""


def validate_stack_sequences(pushed, popped) -> bool:
    if not pushed:
        return True
    stack = []
    i = 0
    for item in pushed:
        stack.append(item)
        while stack and popped[i] == stack[-1]:  # 每添加一个元素，都要判断一下是否可以接连弹出，如果弹不动了再加新的元素。
            stack.pop(-1)
            i += 1

    if stack:  # 如果stack中还有元素则表示pop队列是不成立的
        return False
    else:
        return True