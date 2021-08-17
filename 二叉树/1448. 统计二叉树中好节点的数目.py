# Definition
# for a binary tree node.
"""
给你一棵根为root的二叉树，请你返回二叉树中好节点的数目。

「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。

"""

import doctest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """

        :param root:
        :return:
        >>> self.goodNodes([3,1,4,3,null,1,5])
        """
        if root is None:
            return 0
