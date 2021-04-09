"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
例如输入：
["eat", "tan", "ate", 'tea"]
输出：
[
    ["eat", "ate", "tea"],
    ["tan"]
]

思路：
1. 给字符串排序
2. 使用一个字典，保留某一组单词组成的答案
"""


def group_anagrams(strs):
    final_dict = dict()
    for chars in strs:
        sorted_chars = sorted(chars)  # 排过序后，所有异位词都变成了相同的词。
        sorted_chars = "".join(sorted_chars)
        if sorted_chars not in final_dict:
            final_dict[sorted_chars] = [chars]
        else:
            final_dict[sorted_chars].append(chars)
    return list(final_dict.values())
