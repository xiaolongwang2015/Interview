"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，
返回-1。
你可以认为每种硬币的数量是无限的。
"""
import sys


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            coin_list = []
            for coin in coins:
                if i - coin < 0:
                    coin_list.append(sys.maxsize)
                else:
                    coin_list.append(dp[i - coin])
            if min(coin_list) == sys.maxsize:
                dp[i] = sys.maxsize
            else:
                dp[i] = min(coin_list) + 1
        return -1 if dp[amount] == sys.maxsize else dp[amount]


class Solution2:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    test = Solution()
    print(test.coinChange([2147483647], 2))
