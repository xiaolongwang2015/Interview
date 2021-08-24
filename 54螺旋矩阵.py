"""
54 螺旋矩阵
难度：中等
题目描述：
        给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
示例1：
        输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
        输出：[1,2,3,6,9,8,7,4,5]
示例2：
        输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        输出：[1,2,3,4,8,12,11,10,9,5,6,7]

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

题解方法：

"""
from itertools import product
from collections import deque


def spiralOrder(matrix: list) -> list:
    """
    按照顺时针螺旋顺序 ，返回矩阵中的所有元素
    Note: 1 起始元素索引matrix[0][0]
          2
    :param matrix:
    :return:
    >>> spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]
    >>> spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    """
    rst = []
    idx_collection = list(product(range(len(matrix)), range(len(matrix[0]))))
    row_idx, column_idx = 0, 0  # 起始元素索引matrix[0][0]
    idx_collection.remove((row_idx, column_idx))
    rst.append(matrix[row_idx][column_idx])
    direction = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])
    direction_row, direction_column = direction.popleft()
    direction.append([direction_row, direction_column])
    while True:
        if not idx_collection:
            break

        if (row_idx + direction_row, column_idx + direction_column) not in idx_collection:
            direction_row, direction_column = direction.popleft()
            direction.append([direction_row, direction_column])
        row_idx += direction_row
        column_idx += direction_column
        idx_collection.remove((row_idx, column_idx))
        rst.append(matrix[row_idx][column_idx])
    return rst


def direction_gen():
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for direction in directions:
        yield direction


if __name__ == '__main__':
    import doctest

    doctest.testmod()
