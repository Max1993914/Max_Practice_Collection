"""
跳跃游戏，给定一个非负整数数组nums，你最初位于数组的第一个下标。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
例如输入:[2,3,1,4]
输出:true
index0时先跳一步到index1,然后跳2步到最后一个index。

思路：贪心算法
每个数值表示在这一点可以跳跃的"最大"长度，意味着如果能到达某一个位置，就能到达它前面的所有位置。
因此，只需要遍历数组，并且每次记录最远跳跃距离即可，只要这个最远距离最后大于等于最后一个元素下标即返回True
"""


def can_jump(nums):

    max_i = 0
    for i, distance in enumerate(nums):
        if i <= max_i:
            max_i = max(max_i, i + distance)
    return max_i >= len(nums) - 1


lis1 = [2, 4, 1, 1, 0]
assert can_jump(lis1) is True

lis2 = [1, 0, 2]
assert can_jump(lis2) is False
