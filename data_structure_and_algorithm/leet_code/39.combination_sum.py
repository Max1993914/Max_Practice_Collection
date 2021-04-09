"""
组合总和
给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
数字可以被重复使用
例如：candidates = [2, 3, 6, 7]， target  = 7
输出:
[
    [7],
    [2, 2, 3]
]

思路：回溯算法
                    0
             0+2               0+3        0+6         0+7(bingo)
     0+2+2   0+2+3   0+2+6(break) ...
0+2+2+2 0+2+2+3(bingo) ....
"""
import copy


def combination_sum(candidates, target):
    length = len(candidates)
    all_results = []
    results = []
    res = target

    def back_trace(index):
        nonlocal res
        if res == 0:
            all_results.append(copy.deepcopy(results))
            return
        elif res < 0:
            return

        for i in range(index, length):
            results.append(candidates[i])
            res -= candidates[i]
            back_trace(i)
            results.pop(-1)
            res += candidates[i]

    back_trace(0)
    return all_results
