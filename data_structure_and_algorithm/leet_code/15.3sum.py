"""
给你一个包含n个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为0且不重复的三元组。
不允许同一个数字使用两次。
思路：
0. 边界检查：数组中元素不能小于3个。
1. 先排序
2. 去重复：
    如果nums[i]>0，立即停止遍历并返回，因为排过序了，求和一定大于0了。
    如果i>0 且 nums[i] == nums[i-1]，则跳过这次遍历，因为nums[i]情况下所取的left和right是nums[i-1]的子集。
3. 索引i遍历数组，每次遍历时维持两个左右索引left和right，left=i+1，right=n-1。
    当nums[i]+nums[left]+nums[right] = 0时记录下来。然后分别判断left和right是否和其下一个数重复，如果重复则跳过。
4. 如果nums[i]+nums[left]+nums[right] >0，说明right太大，right -=1
5. 如果nums[i]+nums[left]+nums[right] <0，说明left太小，left +=1
时间复杂度：O(n**2)
空间复杂度：O(n),实际情况下可能不允许原数组改动，所以需要对排序生成的nums副本进行额外的空间分配。
"""


def three_sum(nums):
    length = len(nums)
    result = []
    nums = sorted(nums)
    if length < 3:
        return result
    for i in range(length-2):
        if nums[i] > 0:
            return result  # 后面3个数之和只能大于0
        if i > 0 and nums[i] == nums[i-1]:
            continue  # 这种情况下，i的组合只能是i-1的子集
        left = i+1
        right = length-1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                result.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
    return result


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))







