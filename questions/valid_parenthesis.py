# -- encoding:utf-8 --
"""
题目：有效的括号
难度：简单

题目描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：1左括号必须用相同类型的右括号闭合。2左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


def is_valid(s: str) -> bool:
    """
    解题思路：栈
    复杂度分析：
        时间复杂度：O(n)O(n)，其中 nn 是字符串 ss 的长度。
        空间复杂度：O(n + |\Sigma|)O(n+∣Σ∣)，其中 \SigmaΣ 表示字符集，本题中字符串只包含 66 种括号，
                   |\Sigma| = 6∣Σ∣=6。栈中的字符数量为 O(n)O(n)，而哈希映射使用的空间为 O(|\Sigma|)O(∣Σ∣)，相加即可得到总空间复杂度。

    :param s:
    :return:
    """
    if len(s) % 2 == 1:
        return False

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack


if __name__ == '__main__':
    print(is_valid('{[({})]}'))
    print(is_valid('{[(]})'))
