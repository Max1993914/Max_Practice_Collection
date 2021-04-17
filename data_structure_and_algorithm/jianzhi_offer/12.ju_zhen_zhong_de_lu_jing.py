# -*- coding: utf-8 -*-
"""
矩阵中的路径
给定一个m x n 二维字符网格board和一个字符串单词word 。如果word存在于网格中，返回true；否则，返回false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

|a|b|c|e
|s|f|c|s
|a|d|e|e
word=bcce 结果为True

思路：回溯+剪枝
1. 由于路径可以从任意位置开始，所以需要循环开启初始函数
2. 以下几种情况剪枝：
    i,j越界
    当前位置board[i][j] != word(index)
    当前位置board[i][j] 已经被访问过
3. 当index = len(word) -1 的时候就表示已经全部匹配成功了。
"""


def exist(board, word: str) -> bool:
    m = len(board)
    n = len(board[0])

    def recur(i, j, index):
        if i >= m or i < 0 or j >= n or j < 0:  # 越界
            return False
        if board[i][j] != word[index]:  # 当前位置不匹配字符
            return False
        if index == len(word) - 1: return True  # 已经匹配当前字符，并且index已经到达word末尾，则表示已经全部匹配
        board[i][j] = " "  # 将当前位置值置为空格，作为一种标记，表示"已访问过"
        res = recur(i + 1, j, index + 1) or recur(i - 1, j, index + 1) or recur(i, j + 1, index + 1) or recur(i, j - 1,
                                                                                                              index + 1)
        board[i][j] = word[index]
        return res

    for i in range(m):  # 由于可能从任意位置开始，i，j需要遍历
        for j in range(n):
            has = recur(i, j, 0)
            if has:
                return has
    return False