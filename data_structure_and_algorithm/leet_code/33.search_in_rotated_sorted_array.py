"""
搜说旋转排序的数组
数组是经过旋转的，例如[4,5,6,7,0,1,2,3]。搜索这种旋转数组中是否存在某个数target，返回其下标，否则返回1。
例如输入：[4,5,6,1,2,3], 5
输出：1

思路：二分法。
1. 旋转数组先选取中间下标mid，至此至少有一边是完全有序的。
2. 首先判断nums[mid]是否是target，如果是直接返回。
3. 如果左边是完全有序的话，就继续判断target是否在这个范围内，如果在说明target在左边，否则在右边。
"""


def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:  # 左侧为完整升序
            if nums[left] <= target < nums[mid]:  # target 在left到mid中间
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] >= target > nums[mid]:  # 右侧为完整升序
                left = mid + 1
            else:
                right = mid - 1
    return -1


lis1 = [4, 5, 6, 7, 0, 1, 2]
assert search(lis1, 5) == 1
lis2 = [4, 5, 6, 7]
assert search(lis2, 8) == -1

