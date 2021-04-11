"""
只出现一次的数字：
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

思路1：使用字典记录数量

时间复杂度：O(n)
空间复杂度: O(n)

思路2：异或
2和4异或，因为2=010， 4=100，所以异或后为110=6。
异或有以下特性：
1. 任意数和0异或都是它自己
2. 任意数和自己异或都是0
3. 异或满足交换律和结合律：a^b^a = (a^a)^b = 0^b = b
时间复杂度：O(n)
空间复杂度：O(1)
"""
import functools


# 思路1
def single_number1(nums):
    dic = dict()
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    for key, value in dic.items():
        if value == 1:
            return key


# 思路2
def single_number2(nums):
    return functools.reduce(lambda x, y: x ^ y, nums)
