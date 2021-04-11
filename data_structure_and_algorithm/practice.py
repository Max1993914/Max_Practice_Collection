def bubble_sort(nums):
    for i in range(len(nums)-1):
        is_bubble = False
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_bubble = True
        if not is_bubble:
            break
    return nums


a = [2, 4, 1, 6, 10, 7, 5]
print(bubble_sort(a))
# 时间复杂度：最坏o(n**2)， 最好o(n), 平均o(n**2)
# 空间复杂度o(1)
# 稳定


def insert_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        insert_pos = 0
        for j in range(i-1, -1, -1):
            if nums[j] > temp:
                nums[j+1] = nums[j]
            else:
                insert_pos = j+1
                break
        nums[insert_pos] = temp
    return nums


b = [3, 4, 1, 6, 2, 10, 7, 5]
print(insert_sort(b))
# 时间复杂度：最好on，最坏on**2，平均on**2
# 稳定
# 原地排序


def selection_sort(nums):

    for i in range(len(nums)-1):
        min_num = nums[i]
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < min_num:
                min_num = nums[j]
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums


c = [3, 4, 111, 6, 2, 10, 7, 5]
print(selection_sort(c))
# 原地排序
# o(n**2)
# 不稳定


def quick_sort(nums):

    def recur(start, end):
        if start >= end:
            return
        pivot = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        recur(start, i-1)
        recur(i+1, end)

    recur(0, len(nums)-1)
    return nums


d = [1, 2, 11, 6, 3, 10, 7, 5, 11]
print(quick_sort(d))


# merge sort
def merge_sort(nums):

    def recur(start, end):
        merged = []
        if end <= start:
            return
        mid = (start+end)//2
        recur(start, mid)
        recur(mid+1, end)

        # merge
        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if nums[i] < nums[j]:
                merged.append(nums[i])
                i += 1
            else:
                merged.append(nums[j])
                j += 1

        if i <= mid:
            merged.extend(nums[i:mid+1])

        if j <= end:
            merged.extend(nums[j:end+1])
        nums[start:end+1] = merged
        return nums

    new_nums = recur(0, len(nums)-1)
    return new_nums


e = [1, 2, 9, 11, 6, 3, 10, 7, 5, 11, 16]
print(merge_sort(e))


# 前k个元素
# 使用快速排序降序：当i=2，k=3时，nums[i]就是第三个，否则如果k>nums[i]，则继续在右边找
def find_k(nums, k):

    start = 0
    end = len(nums)-1

    def recur(start, end, k):
        if start > end:
            return

        pivot = nums[end]
        i = start
        for j in range(i, end):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[end], nums[i] = nums[i], nums[end]
        if i == k-1:
            return nums[i]
        elif i > k-1:
            return recur(start, i-1, k)
        else:
            return recur(i+1, end, k)

    result = recur(start, end, k)
    return result


ff = [14, 2, 10, 6, 9, 3, 1, 7]
print(find_k(ff, 5))


























