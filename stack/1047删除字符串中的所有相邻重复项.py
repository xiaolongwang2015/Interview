"""
给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return s

        stack = list()
        for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
            else:
                stack.pop(-1)
                continue
        return ''.join(stack)


if __name__ == '__main__':
    test_sample = "abbaca"
    test = Solution()
    print(test.removeDuplicates(test_sample))
