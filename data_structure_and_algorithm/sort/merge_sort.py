"""
归并排序
基本算法：采用分治法，把数组从中间拆成2半，再拆再拆，最后拆成单个数字后再两两组合排序。
        递推公式：Sort(p~r) = Merge(Sort(p~q), Sort(q+1~r))
        递推终止条件：p >= r
是否稳定：稳定。只要在合并两个数组时，当两个元素相同的时候优先放入左侧的元素即可。
空间复杂度：虽然递归的时候会生成一大堆临时列表，但其实在任意时刻只有一个merge函数在运行，也就是说临时数组最大长度也就是n,所以空间复杂度为O(n)
最优时间复杂度：O(nlogn)，递归深度为logn,每一层递归其实都会对每个元素进行排序。
最差时间复杂度：O(nlogn)
平均时间复杂度：O(nlogn)
评价：比冒泡，插入，选择排序速度都要更快，且时间复杂度稳定，不受数组原有有序度影响。但其不是原地排序算法，空间复杂度方面较差。
"""

u = [20, 16, 3, 4, 2, 14, 33, 60, 8, 22, 20]


def merge_sort(unsorted, start_index, end_index):
    if start_index >= end_index:  # 终止条件
        return
    mid_index = (start_index + end_index)//2  # 偶数个元素时，一边一半：奇数个元素时，左边多一个
    merge_sort(unsorted, start_index, mid_index)
    merge_sort(unsorted, mid_index + 1, end_index)

    merge(unsorted, start_index, end_index, mid_index)

    print(unsorted)


def merge(unsorted, start_index, end_index, mid_index):
    temp = []  # 唯一的额外空间，其余代码逻辑通通不需要生成额外的数组
    i = start_index
    j = mid_index + 1
    while i <= mid_index and j <= end_index:
        if unsorted[i] <= unsorted[j]:
            temp.append(unsorted[i])
            i += 1
        else:
            temp.append(unsorted[j])
            j += 1

    if i <= mid_index:
        temp.extend(unsorted[i:mid_index + 1])
    if j <= end_index:
        temp.extend(unsorted[j:end_index + 1])

    unsorted[start_index:end_index+1] = temp


merge_sort(u, 0, len(u)-1)