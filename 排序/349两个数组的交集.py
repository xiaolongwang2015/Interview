"""
给定两个数组，编写一个函数来计算它们的交集。
"""


class Solution:
    def intersection(self, nums1, nums2):
        rst = []
        for num in nums1:
            if num in nums2 and num not in rst:
                rst.append(num)
        return rst


class Solution2:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
