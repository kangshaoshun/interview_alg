#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
"""

class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool

        dfs的应用
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, value = stack.pop()
            if not node.left and not node.right and value == sum:
                return True
            if node.right:
                stack.append((node.right, value + node.right.value))
            if node.left:
                stack.append((node.left, value + node.left.value))
        return False
