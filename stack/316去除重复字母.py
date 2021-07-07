"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        frequency = Counter(s)
        for char in s:
            if char not in stack:
                while stack and char < stack[-1] and frequency[stack[-1]] > 1:
                    frequency[stack.pop(-1)] -= 1
                stack.append(char)
            else:
                frequency[char] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    test_sample = "bbcaac"
    test = Solution()
    print(test.removeDuplicateLetters(test_sample))
