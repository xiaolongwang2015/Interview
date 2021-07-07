# -- encoding:utf-8 --
"""
题目：实现pow(x, n)即x的n次方。
难度：中等
题目描述：实现pow(x, n)即x的n次方。-100 < x < 100, -2**31 <= n <= 2**31-1
"""


def pow_test(x, n: int):
    """
    递归
    :param x:
    :param n:
    :return:
    """
    if n >= 0:
        return mul1(x, n)
    else:
        return 1.0 / mul1(x, -n)


def mul1(x, n):
    if n == 0:
        return 1
    y = mul1(x, n // 2)
    if n % 2 == 0:
        return y * y
    else:
        return y * y * x


if __name__ == '__main__':
    print(pow_test(0, 0))
