"""
全排列
给定一个没有重复数字的序列，返回其所有可能的全部排列
例如输入：[1, 2, 3]
输出：
[
    [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
]
思路：回溯算法
1. 将题目给定的数组nums分成两部分，左边是已填充部分，右边是未填充部分。
2. 遍历数组，每次将一个未填充部分的数填到前面。
                [1, 2, 3]
        [1]           [2]           [3]
  [1,2] [1,3]     [2,1], [2,3]     [3,1] [3,2]
[1,2,3] [1,3,2]  [2,1,3] [2,3,1]  [3,1,2] [3,2,1]
"""
import copy


def permute(nums):
    result = []
    all_results = []
    length = len(nums)

    def back_trace(index):
        if index >= len(nums):
            all_results.append(copy.deepcopy(result))
            return

        for i in range(index, length):
            nums[i], nums[index] = nums[index], nums[i]
            result.append(nums[index])
            back_trace(index + 1)
            result.pop()
            nums[i], nums[index] = nums[index], nums[i]

    back_trace(0)
    return all_results
