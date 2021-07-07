"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 初始化
        left = 0
        start_index = 0
        end_index = 0
        length = 0
        window_dict = {}
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.setdefault(char, 0) + 1
        # 窗口滑动
        for i in range(len(s)):
            if s[i] in t_dict:
                window_dict[s[i]] = window_dict.setdefault(s[i], 0) + 1
            while self.is_valid(window_dict, t_dict) is True:
                if i - left + 1 < length or length == 0:
                    length = i - left + 1
                    start_index = left
                    end_index = i + 1
                if s[left] in t_dict:
                    window_dict[s[left]] -= 1
                    # if window_dict[s[left]] == 0:
                    #     del window_dict[s[left]]
                left += 1
        return s[start_index:end_index]

    def is_valid(self, window_dict, t_dict):
        for k, v in t_dict.items():
            if k in window_dict.keys():
                if v <= window_dict[k]:
                    continue
                else:
                    return False
            else:
                return False
        return True

class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口
        need, window = {}, {}
        for c in t:
            need[c] = need.setdefault(c, 0) + 1  # need = {字符:出现次数}

        left, right = 0, 0
        valid = 0  # 验证window是否满足need条件，valid表示满足条件的字符个数
        start, length = 0, len(s) + 1
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:  # 更新窗口数据
                window[c] = window.setdefault(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left < length:  # 优化结果
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:  # 更新窗口数据
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return s[start:start + length] if length != len(s) + 1 else ''


if __name__ == '__main__':
    test1 = "ADOBECODEBANC"
    test2 = "ABC"
    test = Solution()
    print('rst is :', test.minWindow(test1, test2))
