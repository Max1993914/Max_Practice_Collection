"""
快速排序：
基本算法：选择数组中某一个数据作为pivot（分界点），遍历数组，将小于pivot的放左边，大于pivot的放右边。
    递推公式：Sort(p~r) = Sort(p~q-1) + Sort(q+1~r)
    终止条件：p>=r
是否稳定：不稳定
空间复杂度：O(1)
最优时间复杂度：当pivot选取合适，每次都能刚好将数组二等分时，时间复杂度为O(nlogn)
最差时间复杂度：当原数组全部有序，且每次都选择最后一个元素作为pivot，那么等于n+(n-1)+(n-2)....2+1)=O(n**2)
平均时间复杂度： 大多数情况都是O(nlogn)
与归并排序的区别：快速排序是自上而下的，先分区，再处理子问题。（归并算法自下而上，先处理子问题，再合并）
评价：比较实用的排序方法。
"""

u = [2, 5, 6, 1, 11, 9, 5, 7, 12, 22, 4, 3]


def quick_sort(unsorted_list, start_idex, end_index):
    if start_idex >= end_index:
        return unsorted_list

    mid_index = partition(unsorted_list, start_idex, end_index)

    quick_sort(unsorted_list, start_idex, mid_index-1)
    quick_sort(unsorted_list, mid_index+1, end_index)

    return unsorted_list


def partition(unsorted_list, start_index, end_index):
    """
    1. 选择一个pivot的位置（可以选队尾，也可以随机）
    2. 维持两个指针i和j。i用于记录小于pivot的分界点，j用于遍历数组与pivot进行比较
    3. 如果遍历到的值小于pivot值，i，j互换，并且i++
    4. 遍历完以后，把i与pivot互换。此时就将数组分成了3个部分：小于pivot的部分，pivot，和大于pivot的部分。
    5. 递归解决第一个和第三个部分。
    注意，递归下标必须是p~q-1, q+1~r。递归的数组不能包含q。因为如果数组为[2,1,3],且选择3作为pivot，那么每次分区完毕都是[2,1,3]，会进入无限循环。
    """

    pivot_index = end_index
    print("pivot value:", unsorted_list[pivot_index])
    i = start_index
    for j in range(start_index, end_index):
        if unsorted_list[j] <= unsorted_list[pivot_index]:
            unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
            i += 1
    unsorted_list[i], unsorted_list[pivot_index] = unsorted_list[pivot_index], unsorted_list[i]
    print(unsorted_list, i)
    return i


u = quick_sort(u, 0, len(u)-1)


print("---------------------------------------")
# ----------------------------------------------------------------------------------------------------------------------
# 快速排序的应用：求无序数组中第k大的元素。时间复杂度O(n)
# 以最后一个值为pivot，将待排序数组以快速排序的方式分成3份，u[p~q-1], u[q], u[q+1~r], 降序
# 如果q=K-1，那么说明q是我们要找的元素。（假设K=3，排列完之后q=2,说明q前边有两个值，则q为第三大元素）
# ----------------------------------------------------------------------------------------------------------------------

u2 = [2, 5, 6, 1, 11, 9, 5, 7, 12, 22, 4, 3]


def desc_partition(unsorted_list, start_index, end_index):

    pivot_index = end_index
    i = start_index
    for j in range(start_index, end_index):
        if unsorted_list[j] >= unsorted_list[pivot_index]:
            unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
            i += 1
    unsorted_list[pivot_index], unsorted_list[i] = unsorted_list[i], unsorted_list[pivot_index]
    return i


def find_k(unsorted_list, k, start_index, end_index):
    if start_index > end_index:
        return

    mid = desc_partition(unsorted_list, start_index, end_index)
    if mid + 1 == k:  # mid == k - 1 表示 mid 就是第k大元素
        return unsorted_list[mid]
    elif mid + 1 > k:  # 表示k元素在前半部分
        return find_k(unsorted_list, k, start_index, mid-1)
    else:
        return find_k(unsorted_list, k, mid+1, end_index)


print(find_k(u2, 3, 0, len(u2)-1))  # 22








