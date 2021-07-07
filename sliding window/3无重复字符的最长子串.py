"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


class Solution:
    @staticmethod
    def longest_str(input_str):
        if input_str == '':
            return 0
        left = 0
        length_max = 0
        sub_str = set()
        for i in range(len(input_str)):
            while input_str[i] in sub_str:
                sub_str.remove(input_str[left])
                left += 1
            sub_str.add(input_str[i])
            if len(sub_str) > length_max:
                length_max = len(sub_str)
        return length_max


class SolutionOfficial(object):
    @staticmethod
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        left = -1
        temp = 0
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] > left:
                left = dic[s[i]]
            dic[s[i]] = i
            leng = i - left
            temp = leng if leng > temp else temp
        return temp


class SolutionTest:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        left = 0
        temp_set = set()
        max_length = 0
        for i in range(len(s)):
            while s[i] in temp_set:
                temp_set.remove(s[left])
                left += 1
            temp_set.add(s[i])
            max_length = max(max_length, i - left + 1)
        return max_length


if __name__ == '__main__':
    test1 = "abcabcbb"
    test2 = "qrsvbspk"
    print('rst is :', SolutionTest.lengthOfLongestSubstring(test2))
