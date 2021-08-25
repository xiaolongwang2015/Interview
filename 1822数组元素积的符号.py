import operator
from functools import reduce


class Solution:
    def arraySign(self, nums: list) -> int:
        rst = reduce(operator.mul, nums)
        if rst > 0:
            rst = 1
        elif rst < 0:
            rst = -1
        elif rst == 0:
            rst = 0
        else:
            pass
        return rst
