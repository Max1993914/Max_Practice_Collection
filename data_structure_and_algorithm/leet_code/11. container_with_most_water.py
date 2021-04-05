"""
盛水最多的容器

给你n个非负整数，每个数的索引为横坐标，其值为纵坐标，形成直方图。找出其中两个垂直线，使得其面积最大：
例如输入:[1,8,4,7]
输出：8和7围成容器，面积为7x2=14

思路：
双指针，一个指开头一个指结尾。每次求出面积后，移动高度较小的那个指针。
因为area=min(heights[left], heights[right)*(right-left)。当移动指针，横向距离必然减小，
如果移动较大指针，纵向距离只有可能不变或着变小，那么面积不可能变大。
时间复杂度：O(n)
空间复杂度：O(1)
"""


def max_area(heights) -> int:
    left_index = 0
    right_index = len(heights) - 1
    max_result = 0
    while left_index < right_index:
        min_height = min(heights[left_index], heights[right_index])
        max_result = max(max_result, min_height * (right_index - left_index))
        if heights[left_index] < heights[right_index]:
            left_index += 1
        else:
            right_index -= 1
    return max_result


heights = [1, 4, 7, 3, 2, 5]
assert max_area(heights) == 16
