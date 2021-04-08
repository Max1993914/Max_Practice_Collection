"""
电话号码组合：输入一组2-9组成的数，返回所有可能的字母组合
"2": ["a", "b", "c"],
"3": ["d", "e", "f"],
"4": ["g", "h", "i"],
"5": ["j", "k", "l"],
"6": ["m", "n", "o"],
"7": ["p", "q", "r", "s"],
"8": ["t", "u", "v"],
"9": ["w", "x", "y", "z"]

思路：
回溯算法（dbs）
假设输入是23:
         a       b       c
     ad ae af bd be bf cd ce cf
时间复杂度：O((3**m)*(4**n))，m为对应3个字母的数字个数，n为对应4个字母的数字位数。例如23，共有
    ad ae af bd be bf cd ce cf9种组合，即3*3。
空间复杂度：O(n), n为数字的总位数。主要的空间消耗在于调用栈的深度，深度最多就是n。
"""


def get_all_combine(digits):
    if not digits:
        return []
    all_results = []
    result = []
    length = len(digits)

    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def back_tracking(index):
        if index >= length:
            all_results.append("".join(result))
            return
        alpha_str = phone_map[digits[index]]
        for char in alpha_str:
            result.append(char)
            back_tracking(index+1)
            result.pop(-1)

    back_tracking(0)
    return all_results


digits = "23"
print(get_all_combine(digits))





