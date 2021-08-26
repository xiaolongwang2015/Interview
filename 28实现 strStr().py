"""
28 实现 strStr()
难度：简单
题目描述：
        给你两个字符串haystack 和 needle ，请你在 haystack 字符串中
        找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。

        当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
        对于本题而言，当needle是空字符串时我们应当返回 0 。
        这与 C 语言的strstr()以及 Java 的indexOf()定义相符。

示例1：
        输入：haystack = "hello", needle = "ll"
        输出：2
示例2：
        输入：haystack = "aaaaa", needle = "bba"
        输出：-1
示例3：
        输入：haystack = "", needle = ""
        输出：0

题解方法：

"""


def strStr(haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1
