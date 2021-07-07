"""
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
如果不存在满足条件的子数组，则返回 0 。
"""
from sortedcontainers import SortedList


class Solution(object):
    @staticmethod
    def longestSubarray(nums, limit):
        left = 0
        max_length = 0
        sub_array = SortedList()
        for i in range(len(nums)):
            sub_array.add(nums[i])
            while sub_array[-1] - sub_array[0] > limit:
                sub_array.remove(nums[left])
                left += 1
            max_length = max(max_length, i - left + 1)
        return max_length


if __name__ == '__main__':
    nums = [8, 2, 4, 7]
    limit = 4
    print('rst is :', Solution.longestSubarray(nums, limit))

