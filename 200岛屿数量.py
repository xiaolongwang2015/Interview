"""
给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。


输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

"""


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
    for column_idx in range(len(grid)):
        for row_idx in range(len(grid[0])):
            if grid[column_idx][row_idx] == '1':
                rst += 1
            else:
                continue
    return rst


def island_dfs(grid, column_idx, row_idx):
    grid[column_idx][row_idx] = '0'



# class Solution:
#     def dfs(self, grid, r, c):
#         grid[r][c] = 0
#         nr, nc = len(grid), len(grid[0])
#         for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
#             if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
#                 self.dfs(grid, x, y)
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         nr = len(grid)
#         if nr == 0:
#             return 0
#         nc = len(grid[0])
#
#         num_islands = 0
#         for r in range(nr):
#             for c in range(nc):
#                 if grid[r][c] == "1":
#                     num_islands += 1
#                     self.dfs(grid, r, c)
#
#         return num_islands


if __name__ == '__main__':
    import doctest

    # doctest.testmod()
