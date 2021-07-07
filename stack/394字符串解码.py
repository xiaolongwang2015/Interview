"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的输入

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
"""

from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        rst = ''
        stack = []
        num_stack = deque()
        temp = []
        nums_str = '0123456789'
        for char in s:
            if char in nums_str:
                stack.append(char)
            elif char == '[':
                stack.append(char)
            elif char == ']':
                while stack[-1] not in nums_str and stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop()
                while stack and stack[-1] in nums_str:
                    num_stack.appendleft(stack.pop())
                temp = int(''.join(list(num_stack))) * temp
                num_stack = deque()
                while temp:
                    stack.append(temp.pop())
            else:
                stack.append(char)
        rst = rst.join(stack)
        return rst


if __name__ == '__main__':
    test = Solution()
    sample = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    print(test.decodeString(sample))
