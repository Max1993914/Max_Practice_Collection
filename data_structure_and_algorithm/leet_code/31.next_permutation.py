"""
寻找列表排列的下一个排列：
例如：[1,2,3] -> [1,3,2]
如果已经最大了，则重新返回最小的[3,2,1] -> [1,2,3]

思路：
我们要做的是：找到一个比当前排列大的排列，但这个大的幅度尽可能小。于是需要做到以下几点：
1. 需要把一个较大数换到较小数位置，但这个位置要尽可能靠右。
2. 交换的较大数尽可能小。
3. 较大数换到前面之后，它后面的数要重新排列为升序，升序一定小于降序。

具体代码：
1. 从后向前遍历,查找第一个升序的位置i，这就是要交换的位置。同时，i+1往后的位置必为降序。
2. 再次从后向前遍历，找到第一个大于nums[i]的值的位置j，做到较大数尽可能小。
3. 交换i和j位置的值。此时，j的位置是较小数。由于较大数是第一个大于较小数的，所以较小数前面一定大于等于它，后面也一定小于等于它。
4. 此时i+1到最后必为降序排列，将这些数首尾交换置为升序，至此完成。
5. 当列表已经为最大的情况下，第一步是找不到升序位置的，这样就跳过2，3步直接执行第四步，降序变升序。
"""


def next_permutation(nums):
    # 只有升序才能变大, 升序小于降序
    # 最靠右的升序互换，然后后面的数改为降序，做到变大的幅度尽可能小
    length = len(nums)
    i = length - 2
    while i >= 0:
        if nums[i] < nums[i + 1]:
            break
        i -= 1

    if i >= 0:
        j = length - 1
        while j > i and not nums[j] > nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left = i + 1
    right = length - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1