# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        rst = []
        stack = []
        if root is None:
            return rst
        rst.append([root.val])
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)

        layer_index = len(stack) - 1
        layer_rst = []
        for idx, node in enumerate(stack):
            if idx == layer_index:
                layer_rst.append(node.val)
                rst.append(layer_rst)
                layer_rst = []
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
                layer_index = len(stack) - 1
            else:
                layer_rst.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
        return rst
