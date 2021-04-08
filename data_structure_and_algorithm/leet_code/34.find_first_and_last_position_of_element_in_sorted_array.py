"""
根据一个升序序列nums，查找一个数target的第一个和最后一个位置，如果不存在返回[-1, -1]
例如[4,5,6,6,7] 6
输出：[2,3]

思路：
对数组做两次二分法，第一次找"第一个等于target的数"，第二次找"最后一个等于target的数"。
第一次找的时候，判断nums[mid]如果大于等于target，先记录下位置，但在其左边可能还有，否则就是在其右边可能还有。
第二次找的时候同理。如果nums[mid]小于等于target，先记录下位置，但其右边可能还有。
最后，由于可能没有找到，所以需要对二分到最后的两个位置下标做检查。
"""


def search_range(nums, target):
    if not nums:
        return [-1, -1]

    left_result = -1
    right_result = -1

    # 先找左边界，即第一个等于target的值
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:  # mid大于等于target时，先记录下来, 但有可能左边还有
            left_result = mid
            right = mid - 1
        else:
            left = mid + 1

    if left_result == -1:
        return [-1, -1]

    # 再找右边界，即最后一个等于target的值
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:  # mid小于等于target时，先记录下来，可能右边还有
            right_result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(left_result, right_result)

    # 检查是否正确找到位置。
    if left_result <= right_result and nums[left_result] == target and nums[right_result] == target:
        return [left_result, right_result]
    return [-1, -1]


lis = [4, 5, 5, 6, 7, 8]
assert search_range(lis, 5) == [1, 2]
lis2 = [3, 5, 6, 7, 7, 7, 8, 8]
assert search_range(lis2, 7) == [3, 5]
lis3 = [4, 5, 7, 9]
assert search_range(lis3, 6) == [-1, -1]