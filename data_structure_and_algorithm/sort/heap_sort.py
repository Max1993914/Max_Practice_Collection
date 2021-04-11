"""
堆与堆排序
堆：堆是一种完全二叉树，堆中某一个节点的值都必须大于等于（大顶堆）或小于等于（小顶堆）其子树中每一个值。
完全二叉树非常适合用数组来保存，所以堆也同样适宜：
[null, 7, 5, 6, 4, 2, 1]
  0    1  2  3  4  5  6
根节点的索引为i，其左节点索引为i*2, 右节点索引为i*2+1。
对于完全二叉树来说，下标从n//2 + 1到n的节点都是叶子节点，只需要从下标为n//2的节点开始堆化即可。
堆排序包含两步：建堆和排序
1.建堆
    (1) 从最后一个非叶子节点开始到根节点结束，对二叉树中的节点进行堆化
    (2) 堆化：自上而下依次与自己的子节点比大小，如果发现不符合堆的定义则交换元素。
2. 排序
    (1) 把堆顶的元素放到最底部，然后把剩下n-1个元素重新处理成堆即可。（这里的堆化只需要对堆顶元素做一次就可以了）
时间复杂度：O(nlogn)，其中每次堆化需要O(logn）, 共需要n次，所以是O(nlogn)
空间复杂度：O(1)
稳定性：不稳定，由于需要把堆顶元素放到最底部，这种操作会改变相同数据在原始数列的顺序。

评价：堆排序的各项指标与快速排序接近，且更加稳定，但整体性能仍然不如快速排序。原因在于：
1. 由于堆化和排序操作都是跳着访问数组的，这样做堆cpu缓存不友好。
2. 建堆操作会打乱原有数组的顺序，使有序度降低（把大的放在前边）
"""


def build_heap(nums):
    mid = len(nums) // 2
    nums.insert(0, None)  # 插入哨兵元素，使得其更方便通过下标处理
    for i in range(mid, 0, -1):
        heapify(nums, len(nums)-1, i)
    print("built heap:", nums)


def heapify(nums, end_index, index):
    max_pos = index
    while True:
        if index*2 <= end_index and nums[index] < nums[index*2]:
            max_pos = index * 2
        if index*2 + 1 <= end_index and nums[max_pos] < nums[index*2+1]:
            max_pos = index*2 + 1
        nums[max_pos], nums[index] = nums[index], nums[max_pos]
        if max_pos == index:
            break
        index = max_pos


def sort(nums):
    build_heap(nums)
    k = len(nums) - 1
    while k > 1:
        nums[1], nums[k] = nums[k], nums[1]
        k -= 1
        heapify(nums, k, 1)


a = [1, 4, 10, 6, 2, 7, 8, 12, 5]
sort(a)
print(a)