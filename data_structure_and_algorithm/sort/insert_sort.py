"""
插入排序
基本算法：一次插入会选择一个元素，与前面逐个元素进行对比，如果发现顺序不对则继续向后，否则会就地插入。
    比如[1,3,2]，先开始比较3，发现3和1的顺序正确不用动，然后开始比较2，发现2需要在3前边，于是插入1和3之间。
是否稳定：稳定
空间复杂度：原地排序O(1)
最优时间复杂度：完全有序情况，只需要遍历一次待插入数据，发现无需插入，O(n)
最差时间复杂度：完全倒序，遍历待插入数据共(n-1)次,并且都要移动，总操作次数为(n-1)*1+(n-1)*2+...(n-1)*(n-1)。为O(N**2)
平均时间复杂度：在数组中插入一个元素并保持有序，复杂度是O(n)，于是插入排序只要执行n-1次这样的操作就好了，所以平均复杂度O(n)
评价：比冒泡排序好一些。首先两者比较的时间复杂度相同，冒泡交换与插入时移动元素的次数相同（都是逆序度），但不同的是，冒泡在做
    冒泡的交换操作需要3个赋值操作，但插入操作只需要一个一个赋值操作。从这里看插入更快。
"""

u = [11, 2, 5, 10, 6, 7, 9, 2, 4, 13]


def insert_sort(unsorted):
    print("before started:", unsorted)

    for i in range(1, len(unsorted)):  # 从第二个元素开始，作为待比较元素
        insert_pos = 0
        insert_value = unsorted[i]
        for j in range(i-1, -1, -1):  # 逐一与前面元素比较
            if unsorted[j] > insert_value:
                unsorted[j+1] = unsorted[j]  # 移动
            else:
                insert_pos = j+1  # 插入
                break
        unsorted[insert_pos] = insert_value
        print(unsorted)
    return unsorted


u = insert_sort(u)



