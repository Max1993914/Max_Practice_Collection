# -*- coding: utf-8 -*-
"""
旋转数组中的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1

思路：二分法
其实就是查找到这个数组的"旋转点"
1. 首先获取mid的位置，然后判断：
    如果nums[mid] > nums[end],则mid位于左侧旋转序列，我们应该在其右侧查找最小值，start=mid+1
    如果nums[mid] < nums[end],则mid位于右侧旋转序列，我们应该在其左侧查找最小值，end = mid （因为mid有可能最小）
    如果nums[mid] = nums[end],无法判断，则end=end-1缩小范围 (例如[1,1,1,0,1] 和 [1,0,1,1,1])
2. 最后如果start >= end时，直接返回nums[start]即可。

为什么mid要和end比较而不能和start比较呢？因为如果mid>start，无法判断mid在左还是在右：
例如[1, 2, 3, 4, 5]，mid为2，它属于右侧
[3,4,5,1,2],mid还是2，它属于左侧

为什么end=end-1可以缩小范围？
假设旋转点位置为x
如果x < end， 那么end = end-1自然安全
如果x = end:
    1. 此时nums[m] = nums[x] = nums[end], 由于x是旋转点，nums[m] <= nums[i]
    2. 因为m是向下取整，所以i < end, 所以i < x, 所以m必然在左侧数组中，所以nums[m] >= nums[i]。
因此！nums[m] = nums[i]，并且nums[i] ... nums[m] 都等于 nums[x]。虽然end = end - 1 丢失了旋转点，
但是由于此时已经只剩下左侧数组，以后再二分势必只会向左，最终返回的是本轮的nums[i]，而nums[i] = nums[x]
"""


def min_array(numbers):
    start = 0
    end = len(numbers) - 1
    while start < end:
        mid = (start + end) // 2
        if numbers[mid] < numbers[end]:
            start = mid
        elif numbers[mid] > numbers[end]:
            end = mid + 1
        else:
            end = end - 1

    return numbers[start]