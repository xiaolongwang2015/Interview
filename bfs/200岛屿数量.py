"""
200 岛屿数量
难度：中等
题目描述：
        给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
        岛屿总是被水包围，并且每座岛屿只能由水平方向和或竖直方向上相邻的陆地连接形成。
        此外，你可以假设该网格的四条边均被水包围。
示例1：
        输入：grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        输出：1
示例2：
        输入：grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        输出：3

题解方法：
        1.dfs
        2.bfs
        3.并查集
"""

import collections


def numIslands(grid: list) -> int:
    """
    根据输入矩阵求解岛屿数量
    Note: 1.输入空列表
          2.输入类型错误
          3.网格四周均被水包围
    :param grid: 0表示水 1表示陆地
    :return: 岛屿数量
    测试样例：
    >>> numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    1
    >>> numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
    3
    >>> numIslands([[]])
    0
    """
    rst = 0
    row = len(grid)
    column = len(grid[0])
    for row_idx in range(row):
        for column_idx in range(column):
            if grid[row_idx][column_idx] == '1':
                rst += 1
                island_dfs(grid, row_idx, column_idx, row, column)
            else:
                continue
    return rst


def island_dfs(grid, row_idx, column_idx, row, column):
    grid[row_idx][column_idx] = '0'
    for x, y in surround_idx(row_idx, column_idx):
        if 0 <= x < row and 0 <= y < column and grid[x][y] == '1':
            island_dfs(grid, x, y, row, column)

    # if 0 <= row_idx + 1 < row and grid[row_idx + 1][column_idx] == '1':
    #     island_dfs(grid, row_idx + 1, column_idx, row, column)
    # if 0 <= row_idx - 1 < row and grid[row_idx - 1][column_idx] == '1':
    #     island_dfs(grid, row_idx - 1, column_idx, row, column)
    # if 0 <= column_idx + 1 < column and grid[row_idx][column_idx + 1] == '1':
    #     island_dfs(grid, row_idx, column_idx + 1, row, column)
    # if 0 <= column_idx - 1 < column and grid[row_idx][column_idx - 1] == '1':
    #     island_dfs(grid, row_idx, column_idx - 1, row, column)


def island_bfs(grid):
    """

    :param grid:
    :return:
    >>> island_bfs([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    1
    >>> island_bfs([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
    3
    >>> island_bfs([[]])
    0
    >>> island_bfs([["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]])
    58
    """
    rst = 0
    row = len(grid)
    column = len(grid[0])
    queue = collections.deque()
    for row_idx in range(row):
        for column_idx in range(column):
            if grid[row_idx][column_idx] == '1':
                rst += 1
                queue.append([row_idx, column_idx])
                while queue:
                    r_idx, c_idx = queue.popleft()
                    grid[r_idx][c_idx] = '0'
                    for x, y in surround_idx(r_idx, c_idx):
                        if 0 <= x < row and 0 <= y < column and grid[x][y] == '1' and [x, y] not in queue:
                            queue.append([x, y])
    return rst


def surround_idx(row_idx, column_idx):
    yield row_idx + 1, column_idx
    yield row_idx - 1, column_idx
    yield row_idx, column_idx + 1
    yield row_idx, column_idx - 1


# class UnionFind:
#     def __init__(self, grid):
#         m, n = len(grid), len(grid[0])
#         self.count = 0
#         self.parent = [-1] * (m * n)
#         self.rank = [0] * (m * n)
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     self.parent[i * n + j] = i * n + j
#                     self.count += 1
#
#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]
#
#     def union(self, x, y):
#         rootx = self.find(x)
#         rooty = self.find(y)
#         if rootx != rooty:
#             if self.rank[rootx] < self.rank[rooty]:
#                 rootx, rooty = rooty, rootx
#             self.parent[rooty] = rootx
#             if self.rank[rootx] == self.rank[rooty]:
#                 self.rank[rootx] += 1
#             self.count -= 1
#
#     def getCount(self):
#         return self.count


# class Solution:
#     def numIslands(self, grid: list) -> int:
#         nr = len(grid)
#         if nr == 0:
#             return 0
#         nc = len(grid[0])
#
#         uf = UnionFind(grid)
#         num_islands = 0
#         for r in range(nr):
#             for c in range(nc):
#                 if grid[r][c] == "1":
#                     grid[r][c] = "0"
#                     for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
#                         if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
#                             uf.union(r * nc + c, x * nc + y)
#
#         return uf.getCount()


if __name__ == '__main__':
    import doctest

    doctest.testmod()
