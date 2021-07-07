# -- encoding:utf-8 --
"""
题目：判断矩形是否重叠
难度：简单

题目描述：
矩形的上下边平行于x轴，左右边平行于y轴。矩形以列表形式表示[x1,y1,x2,y2],(x1,y1)是左下角坐标],
(x2,y2)是右上角坐标，相交面积大于0判定为重叠，只在角和边重叠的两个矩形不算重叠。
"""


def is_rec_overlap1(rec1, rec2):
    """
    如果rec1上下左右都没有完整的rec2时，认为两个矩形相交。
    Notes:1考虑顶点和边重叠时不算重叠 2考虑某一矩形面积为零的情况
    :param rec1:
    :param rec2:
    :return:
    """
    rst = not (rec1[1] >= rec2[3] or  # 上
               rec1[3] <= rec2[1] or  # 下
               rec1[2] <= rec2[0] or  # 左
               rec1[0] >= rec2[2] or  # 右
               rec1[0] == rec1[2] or  # 点或直线
               rec1[1] == rec1[3] or
               rec2[0] == rec2[2] or
               rec2[1] == rec2[3]
               )
    return rst


def is_rec_overlap2(rec1, rec2):
    """
    矩形在x,y轴投影都有重合说明相交
    :param rec1:
    :param rec2:
    :return:
    """
    if min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) and min(rec1[3], rec2[3]) > max(rec1[1], rec2[1]):
        return True
    else:
        return False


if __name__ == '__main__':
    rec_a = [0, 0, 2, 2]
    rec_b = [0.5, 0.5, 1.5, 1.5]
    print(is_rec_overlap1(rec_a, rec_b))
