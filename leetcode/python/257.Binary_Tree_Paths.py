#coding:utf-8
"""
    Given a binary tree, return all root-to-leaf paths
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
            :type root: TreeNode
            :rtype: List[str]
        """
        """
            Time Complexity:O(N)
            Space Complexity:O(N)
        """
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + '->'))
            if node.left:
                stack.append((node.left, ls + str(node.val) + '->' ))
        return res
