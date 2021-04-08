"""
二分法查找（数组需要事先排好序）
"""


def bisection(lis, target):
    left = 0
    right = len(lis) - 1
    while left <= right:
        mid = (left + right) // 2  # 偶数时，mid靠左；
        if lis[mid] == target:
            return mid
        elif lis[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1  # 表示没有找到


lis1 = [1, 4, 6, 6, 7, 8, 10]
assert bisection(lis1, 10) == 6
lis2 = [2, 3, 4, 5, 7, 8, 19]
assert bisection(lis2, 4) == 2
lis3 = [1, 4, 5]
assert bisection(lis3, 6) == -1


