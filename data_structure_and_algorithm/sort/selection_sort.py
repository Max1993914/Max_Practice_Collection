"""
选择排序
基本算法：每次把排序区间的最小值选出来放到开头
是否稳定：不稳定。假设排序[10, 10, 2]，那么当移动2到前面时，两个10就换了位置。
空间复杂度：原地排序O(1)
最优时间复杂度：全部有序，但依然要遍历所有数组，O(n**2)
最差时间复杂度：全部逆序，依然遍历所有数组，只不过多了一个换位操作，忽略不计。0(n**2)
平均时间复杂度：O(n**2)
评价：最差的排序算法，排序时间消耗非常稳定。
"""

u = [11, 2, 5, 10, 6, 7, 9, 2, 4, 13]


def selection_sort(unsorted):
    print("before sorted:", unsorted)
    for i in range(len(unsorted)-1):  # 每轮排序从哪儿开始
        min_value = unsorted[i]
        min_index = i
        for j in range(i, len(unsorted)):  # 遍历一次
            if unsorted[j] < min_value:
                min_value = unsorted[j]
                min_index = j
        unsorted[min_index], unsorted[i] = unsorted[i], unsorted[min_index]
        print(unsorted)
    return unsorted


u = selection_sort(u)
