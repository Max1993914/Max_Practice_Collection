"""
最长回文字符串:

给一个字符串，找出其中的回文子串
例如输入：babad
输出：bab （aba也可以）

思路：动态规划
一个字符串s[i:j+1]是不是回文有两个条件：
    1. 首尾位置的字符相同
    2. 中间的子字符串也得是回文字符串
状态转移方程：
{
   f(i, j) = True  # 如果i==j，即长度为1
   f(i, j) = s[i] == s[j]  # 如果j==i+1, 即长度为2
   f(i, j) = (s[i] == s[j]) and f(i+1, j-1)  # 长度大于2
}
时间复杂度：O(n**2)，n为字符串长度。
空间复杂度：O(n**2)，存储动态规划状态表的空间。
"""


def longest_palindrome(s):
    # 动态规划
    # f(i, j) = f(i+1, j-1) and s[i] == s[j]
    states = []
    length = len(s)
    result = ""
    for i in range(length):
        states.append([False for _ in range(length)])

    for l in range(length):
        for i in range(length):
            j = i + l
            if j >= length:
                break
            if l == 0:
                states[i][j] = True
            elif l == 1:
                states[i][j] = (s[i] == s[j])
            else:
                states[i][j] = (s[i] == s[j]) and states[i + 1][j - 1]

            if states[i][j] and j - i + 1 > len(result):
                result = s[i:j + 1]
    return result


s = "abccbad"
assert longest_palindrome(s) == "abccba"

s2 = "dfacca"
assert longest_palindrome(s2) == "acca"

s3 = "bbbcc"
assert longest_palindrome((s3)) == "bbb"