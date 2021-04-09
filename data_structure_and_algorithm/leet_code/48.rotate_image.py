"""
给定一个二维矩阵，请将图像顺时针旋转90度。
1|2|3     7|4|1
4|5|6  -> 8|5|2
7|8|9     9|6|3


思路：
两层循环，第一层从外至内，决定是哪个圈层进行旋转；第二层则负责交换
"""


def rotate(matrix):
        i = 0
        j = len(matrix)-1
        while i < j:  # i和j框定了矩阵的圈层，i=0，j=len(matrix)-1为最外圈
            add = 0
            while add < j - i:
                # 行和列分别进行交换
                temp = matrix[i+add][j]
                matrix[i+add][j] = matrix[i][i+add]
                matrix[i][i+add] = matrix[j-add][i]
                matrix[j-add][i] = matrix[j][j-add]
                matrix[j][j-add] = temp
                add += 1
            # 缩小一圈
            i += 1
            j -= 1


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix1)
assert matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]