"""
合并区间
数组中有若干个区间，请合并所有重叠的区间，并返回一个不重叠区间的数组。
例如输入：[[1, 3], [2, 6], [8, 10]]
[1,3] 和[2, 6] 有重叠区域，可以合并。最后输出[[1, 6], [8, 10]

思路：
重叠无非就是两个区间a和b，b的左侧在a的范围内。也就是说:b[0] <= a[1]
1. 先按照左侧开始点进行排序，这样所有有可能重叠的区间必然是连续的
2. 将第一个区间放入merged数组中，接着遍历剩下区间，然后依次判断：
    如果b[0]<=a[1]的话，就可以合并两个区间，即a[1] = max(a[1], b[1])
    否则表示不能合并。
"""


def merge(intervals):
    if len(intervals) == 1:
        return intervals

    sorted_lis = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_lis[0]]
    for i in range(1, len(sorted_lis)):
        if merged[-1][1] < sorted_lis[i][0]:
            merged.append(sorted_lis[i])
        else:
            merged[-1][1] = max(merged[-1][1], sorted_lis[i][1])

    return merged


lis1 = [[1, 3], [2, 4], [5, 8]]
assert merge(lis1) == [[1, 4], [5, 8]]
