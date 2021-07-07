"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        stack = []
        p_dict = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in p_dict:
                stack.append(char)
            else:
                if len(stack) > 0:
                    pass
                else:
                    return False
                if p_dict[stack[-1]] == char:
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    rst = Solution.isValid("(]")
    print(rst)
