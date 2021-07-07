class Wall:
    """
    墙
    """

    def __init__(self, wall_coordinates, wall_type):
        # 设置属性
        self.wall_coordinates = wall_coordinates  # 墙的坐标点集
        self.wall_type = wall_type  # 墙的类型


class Window:
    """
    窗户
    """

    def __init__(self, window_coordinates, need_to_be_dismantled, window_height, window_ground_height):
        # 设置属性
        self.window_coordinates = window_coordinates  # 窗户的坐标点集
        self.need_to_be_dismantled = need_to_be_dismantled  # 窗户是否需要被拆除
        self.window_height = window_height  # 窗户高度
        self.window_ground_height = window_ground_height  # 窗户据地高度


class Column:
    """
    柱子
    """

    def __init__(self, column_type, column_coordinates):
        # 设置属性
        self.column_type = column_type  # 柱子类别 2：圆柱子 1：其他形状柱子
        self.column_coordinates = column_coordinates  # 柱子的坐标点集


class Door:
    """
    门
    """

    def __init__(self, door_type, door_up, door_up2, door_left, door_right, door_curved, door_curved2, door_four_pt,
                 need_to_be_dismantled, door_attribute):
        # 设置属性
        self.door_type = door_type  # 门的类别(单开门双开门)
        self.door_up = door_up  # 门上半部分的坐标点集(如果只有一扇门，数据放在该属性中)
        self.door_up2 = door_up2  # 门第二个上半部分的坐标点集
        self.door_left = door_left  # 门下半部分左边门垛的坐标点集(如果只有一扇门，数据放在该属性中)
        self.door_right = door_right  # 门下半部分右边门垛的坐标点集
        self.door_curved = door_curved  # 门弧形部分的坐标点集  (如果只有一扇门，数据放在该属性中)
        self.door_curved2 = door_curved2  # 门第二个弧形部分的坐标点集
        self.door_four_pt = door_four_pt  # 门的四个点坐标
        self.need_to_be_dismantled = need_to_be_dismantled  # 门是否需要被拆除
        self.door_attribute = door_attribute  # 门的属性（主入口次入口）
