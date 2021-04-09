"""
不同路径：
给一个mxn的棋盘，开始点位于左上角，结束点位于右下角，每次只能向下或向右移动一格。问共有多少条走法？

思路一：回溯（很慢）

思路二：动态规划
状态定义：f(i, j): 到达i，j坐标的路径数量
状态转移方程：f(i, j) = f(i-1, j) + f(i, j+1)
边界条件：f(0, 0) = 1, f(0, ...) 和 f(..., 0) 也都是1
"""
import time


# 回溯
def unique_paths1(m, n):
    result_sum = 0

    def back_trace(index_m, index_n):
        nonlocal result_sum
        if index_m == m - 1 and index_n == n - 1:
            result_sum += 1
            return
        elif index_m > m - 1 or index_n > n - 1:
            return

        back_trace(index_m + 1, index_n)
        back_trace(index_m, index_n + 1)

    back_trace(0, 0)
    return result_sum


def unique_paths2(m, n):
    states = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        states[i][0] = 1

    for j in range(n):
        states[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            states[i][j] = states[i - 1][j] + states[i][j - 1]

    return states[m - 1][n - 1]


assert unique_paths1(3, 7) == unique_paths2(3, 7) == 28
assert unique_paths1(10, 10) == unique_paths2(10, 10) == 48620

# 时间消耗
start = time.time()
unique_paths1(15, 15)
end = time.time()
duration1 = end - start
print("cost:", duration1)

start = time.time()
unique_paths2(15, 15)
end = time.time()
duration2 = end - start
print("cost:", duration2)
print("method 2 is faster than method 1 by {} s".format(duration1-duration2))



