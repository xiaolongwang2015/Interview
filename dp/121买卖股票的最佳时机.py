# -- encoding:utf-8 --
"""
给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""
import copy


class Solution:
    def maxProfit(self, prices) -> int:
        pass


def best_timing(h):
    """
    暴力法
    :param h:
    :return:
    """
    h1 = copy.deepcopy(h)
    h2 = copy.deepcopy(h)
    profit_max = 0
    for i in range(len(h1)):
        for j in range(len(h2)):
            if j <= i:
                continue
            if h1[i] >= h2[j]:
                continue
            profit = h2[j] - h1[i]
            if profit > profit_max:
                profit_max = profit
    return profit_max


def best_timing2(prices):
    """
    一次遍历
    :param prices:
    :return:
    """
    inf = int(1e9)
    min_price = inf
    profit_max = 0
    for price in prices:
        profit_max = max(price - min_price, profit_max)
        min_price = min(price, min_price)
    return profit_max


if __name__ == '__main__':
    print(best_timing2([1, 7, 2, 1, 5, 8]))
