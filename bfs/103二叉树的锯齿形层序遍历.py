"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
"""

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        rst = []
        if root is None:
            return rst

        layer = [root]
        for i in range(10000):
            is_even = True if i % 2 == 0 else False
            rst, layer = self.find_next_layer_nodes(layer, rst, is_even)
            if not layer:
                break
        return rst

    def find_next_layer_nodes(self, layer, rst, is_even):
        current_layer_values = []
        next_layer_nodes = []
        for node in layer:
            current_layer_values.append(node.val)
            if node.left:
                next_layer_nodes.append(node.left)
            if node.right:
                next_layer_nodes.append(node.right)
        # if current_layer_values:
        if is_even is True:
            rst.append(current_layer_values)
        else:
            rst.append(current_layer_values[::-1])
        return rst, next_layer_nodes



