"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
"""
import collections


class Solution(object):
    @staticmethod
    def checkInclusion(s1, s2):
        left = 0
        s1_length = len(s1)
        s2_length = len(s2)
        c1 = collections.Counter(s1)
        c2 = collections.Counter()
        for i in range(s2_length):
            c2[s2[i]] += 1
            if c1 == c2:
                return True
            if i - left + 1 > s1_length:
                c2[s2[left]] -= 1
                if c2[s2[left]] == 0:
                    del c2[s2[left]]
                left += 1
            if c1 == c2:
                return True
        return False


class Solution1(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        c1 = collections.Counter(s1)  # s1的哈希表，实质是字典
        c2 = collections.Counter()  # 实例化一个counter类
        p = q = 0  # 设定下标初始化为0，滑动窗口就是[p,q]
        # 下面就是不断在s2上面进行滑动窗口，不断更新哈希表进行比较，这是采用的边界更新法哦，因此是方法五，而不是方法三
        # 这里补充一下，为什么滑动窗口用while没用for，其实都是一样的，你也可以改成for
        # 但是对于有些情况，就只能用while，比如在回溯算法里面，即循环变量需要频繁的加减，显然此题并不是
        # 因此对于此题，用for也可以，整体来说while的应用场合更加广泛
        while q < l2:
            c2[s2[q]] += 1  # 统计字典哈希表
            if c1 == c2:
                return True  # 注意，这种结果性条件判断一定是写在前面
            q += 1  # s2滑动窗口，下标后移
            if q - p + 1 > l1:  # 为什么有这个呢？因为第一个滑动窗口比较特殊，要先构造第一个完整的滑动窗口，后面才是更新边界
                c2[s2[p]] -= 1  # 字典哈希表移除最前面的字符
                if c2[s2[p]] == 0:  # 由于counter特性，如果value为0，就删除它
                    # 否则会出现s1的map没有a，但是s2的map的a为0，此时是成立的，但是导致了这两个map不相等，结果出错
                    del c2[s2[p]]
                p += 1  # 最前面的下标右移动
        return False  # 遍历所有滑动窗口过后，仍然没返回true，那就是不合题意


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print('rst is :', Solution.checkInclusion(s1, s2))
