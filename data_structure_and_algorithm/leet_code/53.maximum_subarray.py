"""
最大子序列和
给定一个整数数组nums，找到一个具有最大和的联系子数组，返回其最大和
例如输入：[-2, 1, -3, 4, 5]
[4, 5]的和最大，返回9

思路一：动态规划
状态定义：dp[i]表示的是以nums[i]结尾的连续子数组最大和。
dp[i]有两种情况：
dp[i] = {
            dp[i-1] + nums[i]        if dp[i-1]>=0
            nums[i]        if dp[i-1]<0   (如果前面最大子序和为负数，那么加上反而更小，不如不加)
        }
最后要注意，这里的状态定义并不是问题的定义，不能直接返回dp[n]。而应该是max[dp[0],dp[1] ...dp[n])
时间复杂度：O(n)
空间复杂度：O(1)
"""


def max_subarray(nums):
    """动态规划
    f(i) = max(f(i-1) + nums[i], nums[i])
    """
    temp_sum = 0
    max_sum = nums[0]
    for i in range(len(nums)):
        temp_sum = max(temp_sum + nums[i], nums[i])
        max_sum = max(max_sum, temp_sum)
    return max_sum



