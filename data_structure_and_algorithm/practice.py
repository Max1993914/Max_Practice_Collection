def bubble_sort(nums):

    for i in range(len(nums)-1):
        need_next = False
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                need_next = True
        if not need_next:
            break

    return nums


nums = [1, 5, 10, 2, 6, 7, 4, 3]
print(bubble_sort(nums))


def insert_sort(nums):

    for i in range(len(nums)):
        if i == 0: continue

        temp = nums[i]
        index = 0
        for j in range(i-1, -1, -1):
            if nums[j] > temp:
                nums[j+1] = nums[j]
            else:
                index = j + 1
                break
        nums[index] = temp
    return nums


nums = [15, 5, 10, 2, 6, 7, 4, 3, 8]
print(insert_sort(nums))


def selection_sort(nums):

    for i in range(len(nums)-1):
        min_value = nums[i]
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < min_value:
                min_value = nums[j]
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

nums = [15, 5, 10, 2, 6, 7, 4, 3, 8]
print(selection_sort(nums))


def quick_sort(nums):

    def recur(start, end):
        if start > end:
            return
        i = start
        for j in range(start, end):
            if nums[j] < nums[end]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        recur(start, i-1)
        recur(i+1, end)
    recur(0, len(nums)-1)

    return nums

nums = [15, 5, 10, 2, 6, 7, 4, 3, 8]
print(quick_sort(nums))


def merge_sort(nums):

    def recur(start, end):
        if start >= end:
            return

        mid = (start + end)//2
        recur(start, mid)
        recur(mid+1, end)

        i = start
        j = mid + 1
        temp = list()
        while i <= mid and j <= end:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        if i <= mid:
            temp.extend(nums[i:mid+1])
        if j <= end:
            temp.extend(nums[j:end+1])
        nums[start:end+1] = temp

    recur(0, len(nums)-1)
    return nums


nums = [15, 5, 10, 2, 6, 7, 4, 3, 8]
print(merge_sort(nums))


def heapify(nums, start, end):
    while True:
        most_big_index = start
        if start * 2 <= end and nums[most_big_index] < nums[start * 2]:
            most_big_index = start * 2
        if start * 2 + 1 <= end and nums[most_big_index] < nums[start *2 + 1]:
            most_big_index = start * 2 + 1
        if most_big_index == start:
            break
        nums[start], nums[most_big_index] = nums[most_big_index], nums[start]
        start = most_big_index


def build_heap(nums):

    nums.insert(0, None)

    mid = (len(nums) -1)//2
    for i in range(mid, 0, -1):
        heapify(nums, i, len(nums)-1)

    return nums

def sort(nums):
    heap = build_heap(nums)

    for i in range(len(heap)-1, 1, -1):
        heap[1], heap[i] = heap[i], heap[1]
        heapify(heap, 1, i-1)
    return heap

nums = [5, 1, 8, 10, 20, 4, 2, 7, 15, 9]
print(sort(nums))


def bisection(nums, target):

    start = 0
    end = len(nums)-1

    def recur(start, end):
        nonlocal target
        if start > end:
            return -1
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return recur(start, mid-1)
        else:
            return recur(mid+1, end)

    return recur(start, end)

nums = [1, 2, 4, 6, 7, 10, 12, 14, 15, 16]
print(bisection(nums, 15))


def zero_one_backpack(max_weight, nums):
    states = [[False for _ in range(len(nums))] for _ in range(max_weight+1)]
    # 第一个坐标是weight，第二个坐标是nums

    # 第0个物品
    states[0][0] = True
    if nums[0] <= max_weight:
        states[nums[0]][0] = True

    for i, weight in enumerate(nums):
        if i == 0: continue
        # 不放第i个物品
        for j in range(max_weight+1):
            if states[j][i-1] == True:
                states[j][i] = True

        # 放第i个物品
        for j in range(max_weight+1):
            if j + weight <= max_weight and states[j][i-1] == True:
                states[j+weight][i] = True

    for k in range(max_weight, -1, -1):
        if states[k][len(nums)-1]:
            return k

items = [10, 10, 12, 12, 19]
max_weight = 28
print(zero_one_backpack(max_weight, items))  # 24





















































