"""
两数求和：
给定一个值，在列表中找到两个值的和等于它，返回它们的数组下标
例如target=9，list=[2,5,7,3], 则返回[0,2]

思路：
1. 维护一个字典里，键是值，值是数组索引
2. 遍历数组，看 target值-当前值是否在字典里，如果有则找到了两个下标，如果没有就把当前值和索引存入字典
这样只需遍历一次列表即可，查找target-x的复杂度变为O(1)。
时间复杂度O(n)。
空间复杂度O(n)，主要为哈希表开销。
"""


def two_sum(target, l1):

    dic = dict()
    for i, item in enumerate(l1):
        if target-item in dic:
            return [i, dic[target-item]]
        dic[item] = i


target = 7
l1 = [2, 5, 3, 7, 11]
print(two_sum(target, l1))

