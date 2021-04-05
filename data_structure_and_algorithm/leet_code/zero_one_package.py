"""
01背包问题
往一个背包放东西，在不超过背包最大载重的前提下，求能放入物品的最大重量是多少？
解法：动态规划
状态：f(i, cw): i 表示第几个物品，cw表示目前重量。
状态转移表：二维数组，每行表示当前背包的重量，每列表示放不放物品

每个物品放入或者不放入都是一个阶段，且求的是最优解，符合"一个模型"原则。
重复子问题：如果物品的重量为2,2,4，那么放第一个不放第二个和放第二个不放第一个的结果是相同的。
无后效性：每个阶段的决策只关心前一阶段的结果，不用关心前一阶段怎么得来的，也不用担心后一个阶段的影响。
最优子结构：后一个阶段的结果是由前一个阶段的结果得来。放第n个的最优解势必诞生于放第n-1个的解。
"""


def zero_one_package(items, max_weight):
    n = len(items)  # items的数量

    # 初始化state，第一个坐标为item的下标，第二个坐标为当前背包已有重量。保存的值为bool值。
    states = []
    for i in range(n):
        state = [False for _ in range(max_weight+1)]
        states.append(state)

    # 0做哨兵特殊处理
    states[0][0] = True  # 0号物品不放入
    if items[0] <= max_weight:
        states[0][items[0]] = True  # 0号物品放入

    for i in range(1, n):
        for j in range(max_weight+1):  # 不放入当前物品，以第n-1个物品决策阶段的重量为准
            if states[i-1][j] is True:
                states[i][j] = True
        for j in range(max_weight+1-items[i]):  # 放入当前物品
            if states[i-1][j] is True:
                states[i][j + items[i]] = True

    for i in range(max_weight, -1, -1):
        if states[n-1][i] is True:
            return i


items = [10, 10, 12, 12, 19]
max_weight = 28
print(zero_one_package(items, max_weight))  # 24
