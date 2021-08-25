"""
56 合并区间
难度：中等
题目描述：
        以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
        请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例1：
        输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
        输出：[[1,6],[8,10],[15,18]]
        解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例2：
        输入：intervals = [[1,4],[4,5]]
        输出：[[1,5]]
        解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

题解方法：

"""


def merge(intervals: list) -> list:
    """

    :param intervals:
    :return:
    """
    intervals.sort(key=lambda x: x[0])
    rst = []
    for interval in intervals:
        if not rst:
            rst.append(interval)
        if rst[-1][1] >= interval[0]:
            rst[-1][1] = max(rst[-1][1], interval[1])
        else:
            rst.append(interval)
    return rst
