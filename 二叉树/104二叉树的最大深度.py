# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = self.depth_max(root.left, root.right) + 1
        return depth

    def depth_max(self, node_left, node_right):
        if node_left is None and node_right is None:
            return 0
        elif node_left is None and node_right is not None:
            return self.depth_max(node_right.left, node_right.right) + 1
        elif node_left is not None and node_right is None:
            return self.depth_max(node_left.left, node_left.right) + 1
        else:
            return max(self.depth_max(node_left.left, node_left.right),
                       self.depth_max(node_right.left, node_right.right)) + 1
