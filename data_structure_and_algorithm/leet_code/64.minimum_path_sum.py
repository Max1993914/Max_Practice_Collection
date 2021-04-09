"""
最小路径和
给定一个包含非负整数的m x n 网格，请找出一条路径，使得路径上数字之和最小
|1|3|1|
|1|5|1|
|4|2|1|
1-3-1-1-1是最小的，返回7

思路：动态规划
状态定义：dp[i, j]：到达i, j的最小路径和
状态转移方程：
dp[i, j] = min(dp[i-1, j], dp[i, j+1]) + grid[i][j]
边界条件：
dp[0, 0] = grid[0][0]
dp[0, j] = dp[0, j-1] + grid[0][j]
dp[i, 0] = dp[i-1, 0] + grid[i][0]
"""


def min_path_sum(grid):
    m = len(grid)
    n = len(grid[0])

    states = [[0 for _ in range(n)] for _ in range(m)]

    states[0][0] = grid[0][0]

    for i in range(1, m):
        states[i][0] = states[i - 1][0] + grid[i][0]

    for j in range(1, n):
        states[0][j] = states[0][j - 1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            states[i][j] = min(states[i - 1][j], states[i][j - 1]) + grid[i][j]

    return states[m - 1][n - 1]
