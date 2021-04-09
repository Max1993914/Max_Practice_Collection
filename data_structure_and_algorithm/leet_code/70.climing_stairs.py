"""
爬楼梯
假设你正在爬楼梯，需要n阶台阶才能到达楼顶。
每次可以爬一阶或两阶，问有多少种方法可以爬到楼顶？

思路：动态规划
状态定义：f(n): 爬n级台阶的方法数
状态转移方程：由于到达n的时候，可以爬一级，也可以爬两级，所以：
f(n) = f(n-1) + f(n-2)
边界添加：n=1和n=2。
"""


def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    left = 1
    right = 2
    result = 0
    for i in range(3, n + 1):
        result = left + right
        left = right
        right = result

    return result
