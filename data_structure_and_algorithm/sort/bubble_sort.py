"""
冒泡排序
基本算法：在一次冒泡中，挨个比较两个元素，如果顺序不对则换位。一次冒泡至少让一个元素移动到正确的位置
是否稳定：稳定（两个相同的值不会互换位置）
空间复杂度：原地排序O(1)
最优时间复杂度：待排序数组已经完全有序，此时遍历一次数组就可以退出，比较次数为n，交换次数为0，复杂度O(n)
最差时间复杂度：待排序数组完全倒序，需要n + (n-1) +...2 + 1 = O(n**2)
平均时间复杂度：每做一次交换，有序度+1，而平均交换次数为'(最好复杂度次数(0)+最坏复杂度次数(满逆序度)/2', 还是O(n**2)

terms:
有序度：表示数组中有序数对的个数，比如[1,2,4,3]中，有序对有(1,2), (1,4), (1,3), (2,4), (2,3)，有序度为5
(逆序度 = 满有序度 - 有序度）
满有序度 = (n*(n-1))/2
"""

u = [11, 2, 5, 10, 6, 7, 9, 2, 4, 13]


def bubble_sort(unsorted):
    print("before started:", unsorted)
    for i, item in enumerate(unsorted):
        flag = True
        # 无需再判断已经排好了的数
        for j in range(0, len(unsorted)-i-1):  # 一次冒泡的循环
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                flag = False
        # 如果没有发生数据交换，则提前退出
        if flag:
            print("finished!")
            break
        else:
            print("exchange continue")
        print(unsorted)

    return unsorted


u = bubble_sort(u)

