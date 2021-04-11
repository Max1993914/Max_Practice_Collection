"""
买卖股票的最佳时机
给定一个数组prices，它的第i个元素prices[i]表示一支给定股票第i天的价格。
你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回0 。

思路：一次遍历
遍历所有价格，记录每次的最大利润即可。
"""


def max_profit(prices):
    min_price = float("inf")
    max_prof = 0
    for price in prices:
        min_price = min(min_price, price)
        max_prof = max(max_prof, price - min_price)

    return max_prof
