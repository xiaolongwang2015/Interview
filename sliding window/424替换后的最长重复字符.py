"""
题目：替换后的最长重复字符
难度：中等

题目描述：给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换k次。在执行上述操作后，
找到包含重复字母的最长子串的长度。
注意：字符串长度 和 k 不会超过104。

示例：
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
"""


class Solution:
    @staticmethod
    def repeating_char_length(s, k):
        if s == '':
            return 0
        left = 0
        max_length = 0
        char_dict = {}
        for i in range(len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = 1
            else:
                char_dict[s[i]] += 1
            if max(char_dict, key=char_dict.get) + k < i - left:
                left += 1
            if i - left > max_length:
                max_length = i - left


class Solution1:
    @staticmethod
    def repeating_char_length(input_str, k):
        num = [0] * 26
        input_length = len(input_str)
        maxn = left = right = 0

        while right < input_length:
            num[ord(input_str[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(input_str[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(input_str[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left


class SolutionTest:
    @staticmethod
    def repeating_char_length(s, k):
        left = 0
        max_length = 0
        window_dict = 0


if __name__ == '__main__':
    str1 = 'AABCABT'
    k1 = 3
    print(Solution.repeating_char_length(str1, k1))
