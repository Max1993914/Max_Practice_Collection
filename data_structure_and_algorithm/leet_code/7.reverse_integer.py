"""
给你一个32位的有符号整数x ，返回将x中的数字部分反转后的结果。
例如输入：123
输出：321
如果反转后整数超过 32 位的有符号整数的范围 [−2**31,  2**31 − 1]，就返回 0。
思路：
遍历每一位数字，result = result*10 + a_num%10。当最后一位除以10取整为0，表示循环结束。
时间复杂度：O(log(x)), x中大约有log10(x)位数字。 （？）
空间复杂度：O(1)
"""


def reverse(num):

    a_num = abs(num)
    result = 0
    boundry = (1 << 31) if num < 0 else (1 << 31) - 1
    while a_num > 0:
        result *= 10
        result += a_num % 10
        if result > boundry:
            return 0
        a_num = a_num // 10

    return result if num >0 else -result

a = 321

print(reverse(a))
