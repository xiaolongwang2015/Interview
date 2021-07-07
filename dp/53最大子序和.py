"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
"""
import sys


class Solution1:
    """
    动态规划
    """

    def maxSubArray(self, nums) -> int:
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)


if __name__ == '__main__':
    print(sys.maxsize)
