"""
给定一个字符串，找出其中不含重复字符的最长子串长度
例如输入：pwwkew
输出：3 (wke为最长子串)

思路：滑动窗口法
1. 维持一个字典，里面记录所有遇到的字符和它的位置索引，并使用left标记滑动窗口左边界。
2. 遍历字符串，如果没有重复的就把当前字符加入字典，并继续遍历。同时记录最大长度。
3. 如果发现重复字符，移动left到重复字符位置+1的位置，并更新重复字符的字典位置。
    (a)bcabcaa
    (ab)cabcaa
    (abc)abcaa
    a(bca)bcaa  #遇到重复的，移动left到第一个a +1的位置
4. 注意，由于left中记录的重复字符很有可能已经不在滑窗里了，所以left应该是max(left, 重复字符位置+1)
    a(bcd)at
    a(bcda)t  # 此时遇到a，字典里记录过a，但是a已经不在滑动窗口里，所以不算重复字符，left不变。
时间复杂度：O(n)
空间复杂度：O(n)
"""


def longest(s):

    appeared_char_dict = dict()
    left = 0
    max_length = 0
    for i, char in enumerate(s):
        if char in appeared_char_dict:
            left = max(appeared_char_dict[char] + 1, left)
        appeared_char_dict[char] = i
        max_length = max(max_length, i-left+1)
    return max_length

s = "aavpwdacccef"
print(longest(s))  # vpwdac


